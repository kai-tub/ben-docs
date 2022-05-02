# BigEarthNet Guide

:::{warning}
- This site is an initial draft of the BigEarthNet documentation!
- The provided code hasn't passed any internal reviews and should only be copied with caution!
- The first few iterations may contain spelling mistakes and incoherent sentences.
  -  I (Kai) apologies for it in advance. 🙂
:::

This documentation attempts to lower the bar to work with the multi-spectral [BigEarthNet](http://bigearth.net/) dataset.
The BigEarthNet dataset was originally published in {cite:t}`BEN` and
updated in {cite:t}`BEN19labels`.

By providing the following reference, we try to accomplish several goals:

- Provide interested users a high-level overview of the BigEarthNet dataset
  - Where does the data come from?
  - What are _patches_ or tiles?
  - How can I visualize the data?
  - How do I work with the metadata?
  - How do I efficiently work with files?
- Provide pre-calculated files that allow for quick stochastical analysis without requiring any complicated installation or download steps
  - Ideally, (large) CSV files will be generated that allow for fast inspection of the label distributions
  - These files will be created automatically to guarantee reproducibility and easy introspection
- Provide pre-defined splits that allow for easy comparisons among various methods and strategies
- Give _behind the scenes_ details about design decisions that are necessary to work with the data
    - How to work with different spatial resolutions?
    - What interpolation method should be used?
- Provide different optimized approaches to access the dataset to reduce compute-time and power usage greatly
    - Optimizing the way we access the data can lead to significant speed-ups (5--10x)
- Unify our shared knowledge into a single place for our reference

Feel free to let me know about any suggestions!
Either use the public GitHub-based comment section based on [utteranc.es](https://utteranc.es/) or write me an e-mail!
The current progress and the general roadmap will be mainly tracked on the [GitHub project page](https://github.com/kai-tub/ben-docs/projects/1).
Additional ideas/whishes should be discussed in the [Issues](https://github.com/kai-tub/ben-docs/issues) section.


:::{note}
This site will be hosted on GitHub during the development and use [utteranc.es](https://utteranc.es) to enable comments.
The official release of the documentation will be hosted on a different platform.
All previous comments will be deleted after the transition!
:::

<!-- ```{bibliography}
  :filter: docname in docnames
  :labelprefix: Intro-
  :keyprefix: intro-
``` -->
