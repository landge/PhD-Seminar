---
theme: seriph 
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left
title: Figures & Illustrations
mdc: true
---
# Illustrations & Figures

Till Schellhorn, Neuroradiologist, PhD
<!-- First slide -->
---
transition: fade-out
---
# Outline

- <icon-park-stock-market/> Illustrations vs. figures!
  * <logos-matplotlib-icon /> Statistical figures
  * <twemoji-palm-tree /> Illustrations 
- <fluent-emoji-thinking-face /> Why do we need illustrations?
- <noto-hammer-and-wrench /> Tools at our disposal!
  * <mdi-chart-timeline-variant-shimmer /> Statistical plotting software & libraries - online services
  * <logos-adobe-illustrator /> <logos-adobe-photoshop /> Graphics software - online services:w

- <twemoji-robot/> Will AI save us?

<!-- Second slide -->
---
layout: image
image: https://source.unsplash.com/blue-and-clear-body-of-water-K785Da4A_JA 
class: text-center
---

<div class="flex justify-center">
<h2> Why do we need illustrations?</h2>
</div>

---
layout: quote
---

# a poet would be overcome by sleep and hunger before being able to describe with words what a painter is able to depict in an instant. 
Leonardo da Vinci

---
layout:default
---
<img src="/guernica.jpg">

# Guernica
...portrays the suffering of people and animals wrenched by violence and chaos. The work has become a monumental anti-war symbol and a reminder of the tragedies of the Spanish Civil War.

---
layout: section 
---
# Why do we need figures?
[Example](https://observablehq.com/@observablehq/plot-wealth-health-nations)

---
layout: quote
---

# “The simple graph has brought more information to the data analyst’s mind than any other device.” 

John Tukey
---
layout: section
---
# Statistical figures 
## Data visualization

---
layout: image-right
image: https://matplotlib.org/3.3.3/_images/sphx_glr_anscombe_001.png
---
# Anscombe's quartet

Anscombe's quartet is a group of datasets (x, y) that have the same mean, standard deviation, and regression line, but which are qualitatively different.
It is often used to illustrate the importance of looking at a set of data graphically and not only relying on basic statistic properties.

<AutoFitText :max="10" :min="2" modelValue="Source: https://matplotlib.org/3.3.3/gallery/specialty_plots/anscombe.html" />

---
transition: fade-out
---
<style>
  a {
    font-size: .7em;
  }
</style>
# Overlapping density estimations

<div class="flex justify-center">
<img src="https://seaborn.pydata.org/_images/distributions_43_0.png"  />
</div>

<div class="absolute bottom-5 text-gray-700 text-xs">
<a href="https://seaborn.pydata.org/_images/distributions_43_0.png">https://seaborn.pydata.org/_images/distributions_43_0.png</a>
</div>

---
layout:default
---
# Adding visual elements 
* and being consistent with them!
<div grid="~ cols-2 gap-4">

<div>
<img src="/dist_color.png" /> 
</div>

<div>
<img src="/penguins.png" /> 
</div>

</div>



---
layout: section
---
# The grammar of graphics
---
layout: default 
---
# The grammar of graphics

* Not possible to show the syntax for every plotting library, but the underlying principles are the same.
* One tip: Learn the grammar of graphics and you will be able to use (almost) any plotting library!
  * R: ggplot2
  * Python: plotnine, hvplot, seaborn, ...
  * Stata
  * Javascript: Observable, D3.js, ...

---
layout: default
---
# The grammar of graphics (2)

<div class="flex justify-center">
<figure class="max-w-lg">
  <img class="h-auto max-w-full rounded-lg" src="/grammer_of_graphics.png" alt="image description">
  <figcaption class="mt-2 text-sm text-center text-gray-500 dark:text-gray-400">Graphics layers</figcaption>
</figure>
</div>
---
layout: default
---
# Observable notebooks

<img src="/observable.png" />
---
layout: default
title: Instructions and examples
---
# Introduction and examples

* <a href="https://observablehq.com/explore">Explore trending notebooks!</a>
* <a href="https://observablehq.com/d/7105d550682e6500">Examples</a>
* AI - Live coding example.
---
layout: image 
image: https://source.unsplash.com/brown-grass-field-near-mountain-under-white-clouds-during-daytime-CBYShj50si0
title: Next section illustrations
---
<div class="flex justify-center">
<h2> Illustrations </h2>
</div>
---
layout: default
---
# Tips & tricks for good illustrations
* Choose a good color pallette
* Contrast
* Meaning of colors
* Organize the information
* Align the elements
* Consider white space
* Typography
* Hierarchy
* Consistency
---
layout: iframe
url: https://blog.datawrapper.de/beautifulcolors/
title: colors
---

