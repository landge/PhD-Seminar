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
  * <logos-adobe-illustrator /> <logos-adobe-photoshop /> Graphics software - online services
- <twemoji-robot/> Will AI save us?

<!-- Second slide -->
---
layout: section
---
# Why do we need illustrations?

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

---
layout: quote
---

# “The simple graph has brought more information to the data analyst’s mind than any other device.” 

John Tukey
---
layout: iframe
url: https://en.wikipedia.org/wiki/John_Tukey
---
# John Tukey

---
layout: image-right
image: https://matplotlib.org/3.3.3/_images/sphx_glr_anscombe_001.png
---
# Anscombe's quartet

Anscombe's quartet is a group of datasets (x, y) that have the same mean, standard deviation, and regression line, but which are qualitatively different.
It is often used to illustrate the importance of looking at a set of data graphically and not only relying on basic statistic properties.

<AutoFitText :max="10" :min="2" modelValue="Source: https://matplotlib.org/3.3.3/gallery/specialty_plots/anscombe.html" class="text-gray-700 text-s"/>

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

<div class="absolute bottom-5">
<a href="https://seaborn.pydata.org/_images/distributions_43_0.png">https://seaborn.pydata.org/_images/distributions_43_0.png</a>
</div>


---
---
<div class="absolute bottom-5">
The grammar of graphics
</div>