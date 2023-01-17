---
jupytext:
  formats: ipynb,md_representations//md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3.10.9 ('.venv')
  language: python
  name: python3
---

+++ {"tags": []}

# Geographical Patch distribution

The following map shows the geographical label distribution of BigEarthNet.

:::{note}

The polygons have been merged together to minimize page-load time and storage requirements

:::
<!-- # Label Distribution
To visualize the label distribution for each label would require massive amounts of memory and is not easily displayed. 
I am able to visualize the distribution with the help of "datashader", but it would require an active server instance, which is too complicated to maintain for us. 
An alternative could be vegafusion in the future, once it supports GeoJSON, but until then, I won't bother to maintain the server. -->

```{code-cell} ipython3
:tags: []

# remove-input
import warnings

warnings.filterwarnings("ignore")
import geopandas
import folium

# import folium.plugins


def draw_fast_marker_cluster(gdf):
    marker_gdf = gdf.copy()
    marker_gdf = marker_gdf.to_crs("EPSG:4326")
    m = folium.Map(tiles="Stamen Terrain")
    data = marker_gdf.representative_point().apply(lambda point: [point.y, point.x])
    map_data = folium.plugins.FastMarkerCluster(data)
    m.add_child(map_data)
    return m


def simplify_gdf(gdf, tolerance=100):
    geo_series = gdf.geometry.unary_union
    g_series_simp = geo_series.simplify(tolerance)
    return geopandas.GeoDataFrame(
        {"name": ["BigEarthNet-simplified"]}, geometry=[g_series_simp], crs=gdf.crs
    )


# gdf = geopandas.read_parquet("../gdf/raw_ben_s2_gdf_3035.parquet")
# gdf_simp = simplify_gdf(gdf)
# gdf_simp.to_parquet("_static/ben_simple_union.parquet")

gdf = geopandas.read_parquet("_static/ben_simple_union.parquet")
```

```{code-cell} ipython3
# only-dark
# remove-input
gdf.explore(tiles="cartodb dark_matter")
```

```{code-cell} ipython3
# only-light
# remove-input
gdf.explore(tiles="cartodb positron")
```

## Split Distribution

The original training/validation/test split were generated in the following way:
1. Split the original 1200km x 1200km tile into 1.2km x 1.2km patches (as shown in the <a href="#tile-to-patches">Tile to patches figure</a>)
1. Group the patches into 2 x 2 grids
1. Select two patches for the train, one for the validation and one for the test split (as shown in the <a href="#train-split">split figure</a>)

<figure id="tile-to-patches">

:::{include} images/tile-to-patches.excalidraw.svg
:::

  <figcaption>
    <p>
      <span class="caption-text">
        Each 1200km x 1200km tile was split into 1.2km x 1.2km patches
      </span>
      <a class="headerlink" href="#tile-to-patches" title="Permalink to this image">#</a>
    </p>
  </figcaption>
</figure>

<figure id="train-split">

:::{include} ./images/ben-split.excalidraw.svg
:::

  <figcaption>
    <p>
      <span class="caption-text">
      The patches of each tile were grouped into 2 x 2 patches.
      Of those, 2 patches were added to the train split, 1 to the validation and the last one to the test split.
      </span>
      <a class="headerlink" href="#train-split" title="Permalink to this image">#</a>
    </p>
  </figcaption>
</figure>

As a result of this splitting strategy, the splits have a high geographical correlation.
One could argue that this also relates to a high domain correlation, i.e. that the performance on the test split might not provide deep insights into generalizability of the tested model.
