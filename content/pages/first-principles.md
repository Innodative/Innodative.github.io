Title: Information Flow from First Principles
Slug: first-principles
Summary: Notes toward a book on information, uncertainty, and financial markets—published as they are written.

*Information reduces uncertainty about the future.*

That single idea, taken seriously, is the whole program.[^kepler] Build probability from the ground up; put stochastic processes and real market data on that footing; derive the measures—entropy, mutual information, transfer entropy—that make “reduces uncertainty” a number; then follow the numbers outward into directed, higher-order networks of information flow between markets.

<figure class="fig-fan">
<svg viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A return series up to the present, followed by a wide gray fan of possible futures and a narrower red fan conditioned on another series’ past, labeled transfer entropy from X to Y.">
  <line class="ax" x1="40" y1="220" x2="670" y2="220" stroke-width="1"/>
  <line class="ax" x1="40" y1="220" x2="40" y2="30" stroke-width="1"/>
  <line class="grid" x1="380" y1="30" x2="380" y2="220" stroke-width="1" stroke-dasharray="3 4"/>
  <text class="lbl" x="380" y="243" font-size="13" font-style="italic" text-anchor="middle" font-family="Palatino, Georgia, serif">now</text>
  <text class="lbl" x="655" y="243" font-size="13" font-style="italic" text-anchor="end" font-family="Palatino, Georgia, serif">t</text>
  <polyline class="series" points="40,150 62,138 84,158 106,131 128,144 150,120 172,133 194,109 216,126 238,102 260,118 282,96 304,112 326,92 348,104 380,98"
            fill="none" stroke-width="1.6" stroke-linejoin="round"/>
  <path class="fan-g-fill" d="M380,98 L670,20 L670,196 Z" opacity="0.28"/>
  <line class="fan-g-line" x1="380" y1="98" x2="670" y2="20"  stroke-width="1"/>
  <line class="fan-g-line" x1="380" y1="98" x2="670" y2="196" stroke-width="1"/>
  <text class="lbl" x="526" y="72" font-size="13" font-style="italic" transform="rotate(-10.7 526 72)" font-family="Palatino, Georgia, serif">futures of Y alone</text>
  <path class="fan-a-fill" d="M380,98 L670,66 L670,138 Z" opacity="0.18"/>
  <line class="fan-a-line" x1="380" y1="98" x2="670" y2="66"  stroke-width="1.4"/>
  <line class="fan-a-line" x1="380" y1="98" x2="670" y2="138" stroke-width="1.4"/>
  <text class="lbl-accent" x="526" y="105" font-size="13" font-style="italic" transform="rotate(0.8 526 105)" font-family="Palatino, Georgia, serif">given X’s past</text>
  <text class="lbl-strong" x="424" y="181" font-size="15" font-style="italic" font-family="Palatino, Georgia, serif">T</text>
  <text class="lbl-strong" x="433" y="186" font-size="11" font-style="italic" font-family="Palatino, Georgia, serif">X→Y</text>
  <text class="lbl" x="465" y="181" font-size="14" font-style="italic" font-family="Palatino, Georgia, serif">=</text>
  <text class="lbl" x="480" y="174" font-size="14" font-style="italic" font-family="Palatino, Georgia, serif">how much the</text>
  <text class="lbl" x="480" y="190" font-size="14" font-style="italic" font-family="Palatino, Georgia, serif">fan narrows</text>
</svg>
</figure>

## How this is written

The style aims at the Feynman Lectures by way of Tufte: mathematics shown rather than hidden, one evolving toy model as the backbone, and figures that carry real weight.[^figures] The reader these notes are written for is curious, wants to learn, and is not put off by mathematics—none of which is assumed beyond a willingness to follow an argument from the beginning.

Units publish here as they are written. Everything is a draft until the book says otherwise.

## The units

### Part I—Probability, processes, and the data

| | | |
|---|---|---|
| 0 | Data and measurement | *in draft* |
| 1 | What probability is, and getting a feel for it | *planned* |
| 2 | Bayes as the engine | *planned* |
| 3 | Distributions, expectation, and dependence | *planned* |
| 4 | Stochastic processes | *planned* |
| 5 | Market data, and why we transform it | *planned* |
| 6 | Predictive causality, and the spine model | *planned* |

### Part II—Information theory

| | | |
|---|---|---|
| 7 | The core measures | *planned* |
| 8 | Transfer entropy, derived and placed | *planned* |
| 9 | Estimating information from finite samples | *planned* |
| 10 | Why pairwise is not enough | *planned* |

### Part III—Higher-order and networks

| | | |
|---|---|---|
| 11 | Symmetric higher-order information | *planned* |
| 12 | Directed higher-order flow | *planned* |
| 13 | Graphs, graphical models, and information networks | *planned* |
| 14 | Learning the graph: machine learning and PGMs | *planned* |
| 15 | Uncertainty in information networks | *planned* |

### Part IV—Synthesis

| | | |
|---|---|---|
| 16 | Higher-order, multilayer information networks, and synthesis | *planned* |

Off the spine, and skippable: a *pricing sidebar* (binomial pricing to Black–Scholes–Merton, taken for its own sake), a fenced *data-shelf practicum*, and a *workshop appendix*. None of them gates the main path.

[^kepler]: The epistemic posture is Kepler’s: instrument-grade regularities, honestly measured, without a mechanism owed for each one.
[^figures]: The no-orphan-figures rule: every figure is regenerated by a named, seeded notebook, and one build script re-executes them all. Sources live in the [repository](https://github.com/Innodative).
