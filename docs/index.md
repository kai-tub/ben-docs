# BigEarthNet Guide

:::{warning}
- This site should be considered in BETA status and is an active WIP!
:::


:::{note}
<!-- This site is hosted on [GitHub Pages](https://pages.github.com/) and uses [hypothes.is](https://web.hypothes.is/) to enable on-site comments. -->
```{include} ../.github/CONTRIBUTING.md
---
start-after: <!-- hypothesis-pitch-start -->
end-before: <!-- hypothesis-pitch-end -->
---
```

See [](contributing) for more ways to contribute!

:::


```{include} ../README.md
---
start-after: <!-- motivation-start -->
end-before: <!-- motivation-end -->
---
```

Specifically, by providing the following reference, we try to accomplish several goals:

- Provide interested users a high-level overview of the {{ ben }} dataset
  - Where does the data come from?
  - What are _patches_ or tiles?
  - How is the dataset structured?
  - How do I work with the metadata?
  - How can I visualize the data?
- What libraries are available to work with {{ ben }}?
<!-- - Provide pre-calculated files that allow for quick stochastical analysis without requiring any complicated installation or preprocessing steps -->
- Give _behind the scenes_ details about design decisions that are necessary to work with the data
    - How to work with different spatial resolutions?
    <!-- - What interpolation method should be used? -->
- Provide different optimized approaches to access the dataset to reduce compute-time and power usage greatly
    - Optimizing the way we access the data can lead to significant speed-ups (5--10x)

The official paper of the BigEarthNet dataset was initially published in {cite:t}`BEN` and updated to {{ben}} in {cite:t}`BEN19labels`.

```{toctree}
:hidden:

self
basics
data-source

labels
raw-data
patch-distribution

libraries
references
```

```{toctree}
:hidden:

opinionated
```

```{toctree}
:hidden:
:caption: Development

general/contributing
general/code_of_conduct
general/dependencies
general/license
```
