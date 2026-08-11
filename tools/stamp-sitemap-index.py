"""Stamp the sitemap index's <lastmod> values from the children's real contents.

Why this exists. Root sitemap.xml is a sitemap INDEX: it does not list pages, it
lists the two child sitemaps and, for each, the date that child last changed. A
crawler reads those dates to decide whether re-fetching the child is worth it.

The dates were hand-typed, so they went stale the moment a child changed without
anyone remembering to edit this file too. On 2026-08-11 the index still claimed
analyst-prep-kit/sitemap.xml was last touched on 2026-08-07, four days and two new
guides after the fact. A crawler trusting that skips the child and never sees the
new URLs. That is a discovery bug that costs nothing to introduce and is invisible
until you go looking, which is the worst combination.

So: never type these dates again. Each child's lastmod becomes the newest lastmod
found inside it, which is by definition the last time anything in it changed.

Children are read from the local sibling repo when it is there, because that is the
version you are about to push. It falls back to the live URL otherwise.

Usage:
    python tools/stamp-sitemap-index.py            # rewrite sitemap.xml in place
    python tools/stamp-sitemap-index.py --dry-run  # print what would change
"""

import os
import re
import sys
import urllib.request

HOST = "michaelnocito.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "sitemap.xml")

# Each child: the <loc> as it appears in the index, and where to read it from.
# Local paths are relative to the parent of this repo, so a sibling checkout wins
# over the network copy.
CHILDREN = {
    f"https://{HOST}/sitemap-sites.xml": "michaelnocito.github.io/sitemap-sites.xml",
    f"https://{HOST}/analyst-prep-kit/sitemap.xml": "analyst-prep-kit/sitemap.xml",
}

PROJECTS = os.path.dirname(ROOT)


def read_child(loc, rel):
    """Return the child's XML, preferring the local checkout over the live copy."""
    local = os.path.join(PROJECTS, rel.replace("/", os.sep))
    if os.path.exists(local):
        with open(local, encoding="utf-8") as f:
            return f.read(), f"local {rel}"
    with urllib.request.urlopen(loc, timeout=20) as r:
        return r.read().decode("utf-8"), f"live {loc}"


def newest_lastmod(xml):
    """The most recent <lastmod> in a child sitemap, or None if it has none."""
    dates = re.findall(r"<lastmod>\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", xml)
    return max(dates) if dates else None


def main():
    dry = "--dry-run" in sys.argv
    with open(INDEX, encoding="utf-8") as f:
        index = f.read()

    changes = []
    for loc, rel in CHILDREN.items():
        xml, source = read_child(loc, rel)
        newest = newest_lastmod(xml)
        if not newest:
            print(f"  skip  {loc} has no lastmod values")
            continue

        # Match this child's <sitemap> entry and rewrite only its <lastmod>.
        pattern = re.compile(
            r"(<loc>\s*" + re.escape(loc) + r"\s*</loc>\s*<lastmod>)([^<]*)(</lastmod>)"
        )
        m = pattern.search(index)
        if not m:
            print(f"  WARN  no <sitemap> entry found for {loc}")
            continue

        current = m.group(2).strip()
        locs = len(re.findall(r"<loc>", xml))
        if current == newest:
            print(f"  ok    {rel}  {current}  ({locs} urls, from {source})")
            continue

        index = pattern.sub(lambda mm: mm.group(1) + newest + mm.group(3), index, count=1)
        changes.append((rel, current, newest))
        print(f"  STAMP {rel}  {current} -> {newest}  ({locs} urls, from {source})")

    if not changes:
        print("\nnothing to change")
        return

    if dry:
        print(f"\n--dry-run, {len(changes)} change(s) not written")
        return

    with open(INDEX, "w", encoding="utf-8", newline="\n") as f:
        f.write(index)
    print(f"\nwrote {INDEX} ({len(changes)} change(s))")
    print("Commit and push, then the index tells crawlers the child is worth re-reading.")


if __name__ == "__main__":
    main()
