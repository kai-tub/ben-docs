---
jupytext:
  formats: ipynb,md_representations//md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python
  language: python
  name: python3
---

+++ {"tags": []}

# BigEarthNet Labels

BigEarthNet used the [CORINE Land Cover database](https://land.copernicus.eu/pan-european/corine-land-cover) (CLC) of the year 2018 ([CLC2018](https://land.copernicus.eu/pan-european/corine-land-cover/clc2018)) to label 590'326 patches.
The label information about these patches were overlayed with data from the Sentinel-1 and Sentinel-2 mission, to create the datasets BigEarthnet-S1 and BigEarthNet-S2.
BigEarthNet-S2 was the first published dataset and used the _most specific_ version of the classification level of the CLC database, Level-3 with 43 different classes in the dataset {cite}`BEN`.
With the publication of the BigEarthNet-S1 dataset, the recommended label nomenclature has been updated to use a 19-class nomenclature specifically designed for use in the machine-learning domain. {cite}`BEN19labels`.

:::{important}
- The original BigEarthNet-S2 dataset used the CLC Level-3 specification, which defines 44 classes
  - Of these 44-classes one class, `Glaciers and perpetual snow` is not present
  - As a result the label-set is referred to as the 43-label nomenclature.
- The 19-class label nomenclature was introduced to better reflect the application in the machine learning domain
:::

```{code-cell} ipython3
:tags: []

# remove-input
import pandas as pd
import bigearthnet_common.constants as ben_constants
from myst_nb import glue


def style_df(df, th_text_align="left"):
    return df.style.set_properties(**{"text-align": "left"}).set_table_styles(
        [dict(selector="th", props=[("text-align", th_text_align)])]
    )
```

+++ {"tags": []}

(clc-level-3)=
## 43-class nomenclature

+++ {"tags": []}

The CORINE (Coordination of Information on the Environment) Land Cover nomenclature is a nomenclature used to describe physical material at the surface of the earth.
The CLC nomenclature defines a standardized classification schema that can be used for annotating remote imagery.

The CLC classification schema is defined as a 3-level deep hierarchy with:
- 5 classes in level 1
- 15 classes in level 2
- 44 classes in level 3

The following box shows the label hierarchy in a tabular form.
More in-depth information about the CLC2018 nomenclature, including example images for each level-3 label, can be reviewed on the [Corine-Land-Cover-Nomenclature-Guidelines](https://land.copernicus.eu/user-corner/technical-library/corine-land-cover-nomenclature-guidelines/html/index.html) site.

```{code-cell} ipython3
:tags: []

# remove-input
df1 = pd.DataFrame.from_dict(
    ben_constants.CLC_LV3_TO_LV2, orient="index", columns=["CLC_LVL2"]
)
df2 = pd.DataFrame.from_dict(
    ben_constants.CLC_LV3_TO_LV1, orient="index", columns=["CLC_LVL1"]
)
df = df1.join(df2).rename_axis("CLC_LVL3").reset_index()
# require dummy index to apply styling functions, as the Style'r assumes more than only index columns
df = df.reset_index()
df = df.set_index(["CLC_LVL1", "CLC_LVL2", "CLC_LVL3"]).sort_index(level=[0, 1])
clc_styler = style_df(df).hide(axis="columns", subset="index")

glue("clc-table", clc_styler, display=True)
```

+++ {"tags": []}

## 19-class nomenclature

+++ {"tags": []}

The 19-class nomenclature has combined and dropped classes from the 43-class variant for better use in machine learning.
More specifically, ten classes of the original CLC nomenclature are maintained in the new nomenclature, 22 classes are grouped into 9 new classes, and 11 classes have been removed.
Classes that strongly depend on land use or require additional data for their discrimination were removed.

The change was necessary because there are some CLC classes that are difficult to be identified by only exploiting (single-date) Sentinel-2 images, because:
- Land use concepts associated with some classes may not be visible from space or fully recognizable with the spatial resolution of Sentinel-2 images, such as:
    - Dump sites, Sport, and leisure facilities
-  RS time series, which BigEarthNet does not include, may be required to describe and discriminate some classes , such as:
   -  Non-irrigated arable land, or permanently irrigated land

The following table displays the exact the mapping from the old to the new class nomenclature.

<!-- :::{dropdown} 43-class to 19-class label nomenclature

:::{glue:} old2new-labels-table

::: -->

:::{important}
11 classes were dropped from the original 43-class nomenclature.
As a result, there are 57 patches of the original BigEarthNet dataset that have **no** target labels.
These patches should be dropped in experiments to remain compatible with the new nomenclature.
:::

```{code-cell} ipython3
:tags: []

# remove-input
def style_none(val, props=""):
    return props if val is None else None


old2new = (
    pd.DataFrame.from_dict(
        ben_constants.OLD2NEW_LABELS_DICT,
        orient="index",
        columns=["Updated 19-class label"],
    )
    .rename_axis("Original 43-class label")
    .reset_index()
)

styler = style_df(old2new)

styler = (
    styler.hide(axis="index")
    .applymap(style_none, props="color:red")
    .format(na_rep="REMOVED")
)

# glue("old2new-labels-table", styer, display=False)
styler
```

```{code-cell} ipython3
:tags: []


```
