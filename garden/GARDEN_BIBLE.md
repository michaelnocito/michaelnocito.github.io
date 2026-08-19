# The Garden bible

Canon for every guide at https://michaelnocito.github.io/garden/. Read this before
writing or changing one. It sits under `marketing/ARTICLE_STANDARD.md`, which still
governs voice, structure and citations. This file only records what is specific to
growing guides.

Local: `C:\Users\Mike\Projects\michaelnocito.github.io\garden\`
Repo: `michaelnocito/michaelnocito.github.io`, same repo as `art/` and `portfolio/`.
Deploys on push to `main` via GitHub Pages. Pure static, no Jekyll, `.nojekyll` present.

---

## 1. What a guide is for

One job, done with your hands, that a person is about to do today.

Every guide leads with **the ripeness signal, not the instruction**, because deciding
whether it is time is the only hard part of any of these jobs. A head that looks
finished from the front can be three weeks out. A pepper that looks like food can hold
seed that will never sprout.

**One claim per guide, and it has a number or a hard fact in it.** "How to save pepper
seeds" is a list. "Seed scraped out of a green pepper does not sprout, and two weeks on
the counter fixes it" is a claim. If you cannot write the claim in one sentence, the
guide is not ready to write.

---

## 2. The shape of a page

Copy the most recent guide rather than starting from the template in your head. As of
2026-08-19 that is `pepper-seeds/index.html`.

The fixed parts, in order:

1. **Head block.** GA opt-out script, gtag, canonical, description, og tags. Copy it
   whole and change the URLs and text. Never drop the canonical.
2. **Hero.** `mono-label` kicker, `h1` with the `.dot` span, `lede`, `meta-row`. The
   lede carries the payoff. Someone who reads only the lede should already know what
   they get and what it costs them.
3. **`#signal`, labeled "Step zero".** The ripeness test. One `.directive` box holding
   the single visible instruction, then a `.checks` pair, then the photo pair. The
   directive box is the thing that stays on screen while they work, so it is one
   action, not a summary.
4. **The decision section.** Name the fork: the question in one line, the possible
   answers numbered with what each would mean, what decides between them, why it
   matters. Research goes here, in prose with author and year, never at the top.
5. **`#steps`, labeled "The job".** An `<ol class="steps">`, one `h3` per step, a photo
   slot inside each `li`.
6. **The skill section.** The judgement call that separates a decent job from a good
   one. Sorting seed from chaff, or testing whether it is alive.
7. **The catch.** What the reader will get wrong about the result. Cultivars not coming
   back, hybrids splitting, crossing showing up a year late. Every guide has one and it
   is never a reason not to do the job.
8. **`#sources`.** See section 4.
9. **Footer** linking the other guides and the main site.

Available CSS lives in `garden.css` and nothing else is allowed. Classes you have:
`wrap nav mn nav-toggle nav-links hero mono-label dot lede meta-row hr sec-head
sec-label directive k checks check go wait shot shot-pair has-img prose callout steps
vcards vcard sub tbl-scroll tags tag posts post-card kicker btn btn-primary backlink
foot foot-links inline-link soon reveal in`. If a guide seems to need a new class,
it probably needs a different section instead.

**Tables always ship with a `<thead>`.** No exceptions, no bare data blocks.

---

## 3. Photos

### 3a. The slots are invisible, not visual

Every image is a `<figure class="shot">` holding an `<img>` whose `onload` adds
`.has-img` and `.in`. CSS is `.shot{display:none}` and `.shot.has-img{display:block}`.

**An unshot slot renders nothing at all.** No dashed box, no broken icon, no "photo
coming" text. Mike's call, 2026-08-11: visible placeholders made the page look under
construction. A reader sees a finished page with however many photos exist that day.

`.shot-pair` uses `auto-fit`, so a half-shot pair collapses to one full-width photo,
and `:not(:has(.has-img))` hides a pair with neither half filled.

Dropping a correctly named JPG into `garden/img/` makes that figure appear. **No code
edit, no HTML commit.** Every slot records its wanted filename in an HTML comment
directly above the `<img>` and again in `garden/img/PHOTOS.md`.

Accepted tradeoff: each empty slot fires one request that returns the GitHub Pages 404
body, about 9.4KB. It shrinks to zero as slots fill. A manifest would remove the waste
and would also kill the drop-in, so we keep the waste.

### 3b. Photo intake: Mike shoots, Claude names

Set 2026-08-19, when the pepper guide shipped fourteen empty slots.

**Mike never names a file.** He shoots whatever he gets, in whatever order, and hands
over the whole batch with one line saying which guide it was for. That is the entire
job on his end.

Claude then:

1. **Looks at every photo.** Actually opens them. A filename or a thumbnail is not a
   look, and picking a blurry frame because it was listed first is the failure mode.
2. **Picks the single best frame for each slot**, judged against the "why it earns its
   place" column in `PHOTOS.md`, not against which photo is prettiest. A sharp, boring,
   correct shot beats a beautiful one that shows the wrong thing.
3. **Holds the pairs to the same standard.** `pep-01`/`pep-02` and the other pairs have
   to match on angle, distance and light. Two good photos that do not match make a worse
   pair than two average ones that do. If nothing matches, fill neither half and say so.
4. **Renames and drops the winners into `garden/img/`**, then commits and pushes.
5. **Reports back in chat**, in one block: which photo went into which slot, which slots
   are still empty, and for anything rejected, one line on why and what to reshoot. Not
   a file path to a report. The report is the message.

**Never invent a slot to use up a good photo.** If a batch contains something great that
no slot wants, say so and propose the section it would belong to. Adding a figure to the
HTML is a content decision, not a filing decision.

**Never crop or edit beyond a straighten and a resize.** These are documentary photos of
a real job. If it needs retouching to work, it needs reshooting.

### 3c. File rules

- Exact filename from `PHOTOS.md`, lowercase, `.jpg`.
- Naming is `<three letter guide prefix>-NN-slug.jpg`. `sun-`, `zin-`, `bal-`, `pep-`.
- Landscape or square. Portrait works but crops tight in a `.shot-pair`.
- Long edge around 1600px, under about 400KB.
- Shade or overcast for anything outdoors. Plain white or a plain board for anything
  close up.
- Alt text carries the full description, because that is where the words belong for
  anyone who cannot see the photo. The caption underneath is a short line, not a
  second description.

---

## 4. Sources

Numbers come from a university extension service, a peer-reviewed paper, or a
seed-saving organization, and every one is linked at the bottom of the page under
`#sources`.

- **Verify every citation before it ships.** Resolve the DOI. Open the page. If a DOI
  cannot be confirmed, leave it out rather than guess.
- **Give the finding, not just the reference.** Each source line says what that source
  actually told us, so a reader can see why it is there.
- **When sources disagree, say so and give the reader a rule.** The pepper guide has the
  University of Minnesota at one year of storage life and Seed Savers Exchange at three.
  Both are printed, followed by "treat the first spring as the good one and test anything
  older". Picking one silently is worse than showing the split.
- Never a blog, never Wikipedia, never a content farm, as the source of a number. A
  practical growing site can back a technique, and then it is named in the text.

---

## 5. Voice, and the parts that bite here

Everything in `ARTICLE_STANDARD.md` section 2 applies. The parts that matter most on
these pages:

- **Write as Mike, from the row.** First person where it is his garden, and honest about
  what he has and has not done himself.
- **No em-dashes. Never "plain English". Never "gotcha".**
- **One idea per sentence, about fifteen words.** These get read on a phone with one
  hand while the other hand is holding a pepper.
- **Nothing torn down.** Not other methods, not other guides, not the reader's mistake.
  State the fact where it is needed and move on.
- **It has to work spoken.** No "the photo above", no "the table below". A guide with
  empty slots must still read cleanly, which is another reason the slots are invisible.
- **Say the ceiling out loud.** A picked green pepper will never match one ripened on
  the plant. Print that. A guide that oversells its own method gets found out in the
  garden, which is the worst possible place.
- **Generative prompts are unmarked prose.** One prequestion under a heading, one
  self-explanation at the hinge, one imagination prompt after the worked example. No
  boxes, no icons, no "Try this" label. Cap it at four per guide.

---

## 6. Ship checklist

1. Guide folder created, `index.html` written, canonical URL set.
2. Card added to `garden/index.html`, at the top of `.posts`.
3. Photo slots added to `garden/img/PHOTOS.md` with the "what to shoot" and "why it
   earns its place" columns filled, and the total count at the top of that file updated.
4. `sitemap-sites.xml` updated with the new page and the garden hub `lastmod` bumped.
   **Never edit that file with PowerShell `Set-Content`.** It writes a UTF-8 BOM and
   breaks the XML.
5. Footer links on the new guide point at every other guide, and the newest guide is
   added to the older guides' footers when convenient.
6. Every citation resolved and opened.
7. Committed as `Michael Nocito <hello.michaelnocito@gmail.com>`, no AI trailers,
   pushed to `main`.
8. **Deploy verified, not just pushed.** Fetch the live URL and confirm the new page
   returns 200 and contains the h1. A green push is not proof it shipped.
