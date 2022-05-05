# BigEarthNet Guide

:::{warning}
- This site is an initial draft of the BigEarthNet Guide!
- The provided code hasn't passed any internal reviews and should only be copied with caution!
- The first few iterations may contain spelling mistakes and incoherent sentences.
  -  I (Kai) apologies for it in advance. 🙂
:::


:::{note}
This site will be hosted on GitHub during the development and use [hypothes.is](https://web.hypothes.is/) to enable comments.
On the right-hand side, you can access a bar to see comments for the current page and create your annotations by highlighting text and clicking on the `annotate` selection.

- The official release of the documentation will be hosted on a different platform.
- All previous comments will be deleted after the transition!
:::


This documentation reduces the time to work with the multi-spectral {{ ben }} dataset.
The {{ ben }} dataset was initially published in {cite:t}`BEN` and
updated in {cite:t}`BEN19labels`.

By providing the following reference, we try to accomplish several goals:

- Provide interested users a high-level overview of the {{ ben }} dataset
  - Where does the data come from?
  - What are _patches_ or tiles?
  - How is the dataset structured?
  - How do I work with the metadata?
  - How can I visualize the data?
- What libraries are available to work with {{ ben }}?
- Provide pre-calculated files that allow for quick stochastical analysis without requiring any complicated installation or preprocessing steps
- Give _behind the scenes_ details about design decisions that are necessary to work with the data
    - How to work with different spatial resolutions?
    - What interpolation method should be used?
- Provide different optimized approaches to access the dataset to reduce compute-time and power usage greatly
    - Optimizing the way we access the data can lead to significant speed-ups (5--10x)
- Unify our shared knowledge into a single place for our reference
