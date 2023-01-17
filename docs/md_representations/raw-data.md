---
jupytext:
  formats: ipynb,md_representations//md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: 'Python 3.10.4 (''.venv'': venv)'
  language: python
  name: python3
---

+++ {"tags": []}

# Raw BigEarthNet Data

After understanding where the patches come from and how the patches were annotated, the following section will present and discuss the files inside the archives.

+++ {"tags": []}

## BigEarthNet-S2

+++ {"tags": []}

The general contents of the BigEarthNet-S2 archive looks as follows:

```{code-cell} ipython3
:tags: []

# remove-input

from bigearthnet_common.example_data import (
    get_s1_example_folder_path,
    get_s2_example_folder_path,
)
from rich import print
from rich.tree import Tree
from rich.markup import escape
from rich.text import Text
from pathlib import Path
from pydantic import validate_arguments, DirectoryPath
import natsort

ben_s2_path = get_s2_example_folder_path()


def _first_dir_natsort_key(path: Path) -> str:
    """Directories should come first"""
    prefix = 0 if path.is_dir() else 1
    return f"{prefix}{path}"


def _walk_ben_directory(directory: Path, tree: Tree):
    """
    Recursively build a BigEarthNet directory
    """
    # Sort dirs first
    paths = sorted(
        Path(directory).iterdir(), key=natsort.natsort_keygen(_first_dir_natsort_key)
    )
    for path in paths:
        if path.name.startswith("."):
            continue
        if path.is_dir():
            branch = tree.add(
                # f":open_file_folder: [link file://{path}]{escape(path.name)}"
                f":open_file_folder: [bold]{escape(path.name)}"
            )
            _walk_ben_directory(path, branch)
        else:
            text_filename = Text(path.name)
            text_filename.highlight_regex(r".*_\d\d?_", "dim")
            text_filename.highlight_words(["labels_metadata.json"], "bold")
            text_filename.highlight_regex(r"(?<=_).*.tif", "bold")
            # text_filename.stylize(f"link file://{path}")
            icon = "🗺️ " if path.suffix == ".tif" else "📄 "
            tree.add(Text(icon) + text_filename)


@validate_arguments
def walk_ben_directory(directory: DirectoryPath) -> Tree:
    directory = directory.resolve()
    tree = Tree(
        # f":open_file_folder: [link file://{directory}]{directory.name}"
        f":open_file_folder: [bold]{directory.name}"
    )
    _walk_ben_directory(directory, tree)
    return tree


walk_ben_directory(ben_s2_path)
```

+++ {"tags": []}

With the following conventions:
- Each folder corresponds to a single patch
- The `patch_name` is encoded as the name of the folder
- Each patch folder contains a [GeoTIFF](https://en.wikipedia.org/wiki/GeoTIFF) file for each of the 12 bands.
  - The name of the GeoTIFF file is encoded as `<patch_name>_<band>.tif`.
- The [JSON](https://en.wikipedia.org/wiki/JSON) file, named `<patch_name>_labels_metadata.json`, contains the metadata

The prettified contents of a metadata file is:

```{code-cell} ipython3
:tags: []

# remove-input

from rich import print_json
from copy import copy
import json

ben_s2_json_file_paths = list(Path(ben_s2_path).rglob("*.json"))
ben_s2_json_fp = ben_s2_json_file_paths[0]
text = ben_s2_json_fp.read_text()
j = json.loads(text)
simple_j = copy(j)
simple_j["projection"] = simple_j["projection"][:75] + "..."

print_json(data=simple_j)
```

+++ {"tags": []}

- `labels`: Lists the older {ref}`CLC Level-3 nomenclature <clc-level-3>` labels of the patch
- `tile_source`: Shows the source tile that was further processed with [sen2cor](https://step.esa.int/main/snap-supported-plugins/sen2cor/) to generate the atmospherically corrected [L2A](https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-2-msi/level-2a/product-formatting) product tile
- `acquisition_date`: Encodes the acquisition date of the tile in the `YYYY-MM-DD hh:mm:ss` format
- `coordinates`: Encodes the upper left x/y (`ulx`/`uly`) and lower right x/y (`lrx`/`lry`) coordinates of the patch
- `projection`: Relates the values of the `coordinates` to the given coordinate reference systems (CRS)

+++ {"tags": []}

The unshorted (prettified) `projection` entry looks as follows:

```{code-cell} ipython3
:tags: []

# remove-input
import pyproj

print(pyproj.CRS.from_user_input(j["projection"]).to_wkt(pretty=True))
```

+++ {"tags": []}

The `projection` entry encodes the CRS information in the [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_coordinate_reference_systems) format.
For most use-cases, it is sufficient to know, that the combination of the CRS and `coordinates` values define the exact location of a patch.
For more details about what coordinate reference systems are feel free to take a look at one of the following introductory courses:
- [earthdatascience earth-analytics course](https://www.earthdatascience.org/courses/earth-analytics/spatial-data-r/intro-to-coordinate-reference-systems/)
- [gisbooklet](https://bookdown.org/tep/gisbooklet/introduction-to-coordinate-reference-system.html)

+++

## BigEarthNet-S1

```{code-cell} ipython3
# remove-input

ben_s1_path = get_s1_example_folder_path()
walk_ben_directory(ben_s1_path)
```

With the following conventions:
- Each folder corresponds to a single patch
- The `patch_name` is encoded as the name of the folder
- Both bands `VH` and `VV` are saved as an indivdual [GeoTIFF](https://en.wikipedia.org/wiki/GeoTIFF) file
  - The name of the GeoTIFF file is encoded as `<patch_name>_<band>.tif`.
- The [JSON](https://en.wikipedia.org/wiki/JSON) file, named `<patch_name>_labels_metadata.json`, contains the metadata

The prettified contents of a metadata file is:

```{code-cell} ipython3
# remove-input

from rich import print_json
from copy import copy
import json

ben_s1_json_file_paths = list(Path(ben_s1_path).rglob("*.json"))
ben_s1_json_fp = ben_s1_json_file_paths[0]
text = ben_s1_json_fp.read_text()
j = json.loads(text)
simple_j = copy(j)
simple_j["projection"] = simple_j["projection"][:75] + "..."

print_json(data=simple_j)
```

:::{warning}
Compared to the BigEarthNet-S2 metadata file, BigEarthNet-S1:
- calls the date field `acquisition_time` and not `acquisition_date` (S2).
- Encodes the date with `YYYY-MM-DD`T`hh:mm:ss` and not `YYYY-MM-DD hh:mm:ss` (S2)
:::

+++ {"tags": []}

## Metadata Discussion

+++ {"tags": []}

The advantages of having a JSON metadata file in every patch folder are:
1. JSON is a well known data format and has excellent library support
2. JSON is human-readable (not a binary format)
3. Locating the metadata _next_ to the images allows the end-user to easily select subsets of the archive without having to deal with the metadata separately
   - Copying the patches of interest will always include the metadata

The main disadvantages is that each dataset (~80GB) has to be downloaded and that it is not easy to perform statistical analysis.
The metadata files have to be parsed and converted into a common data structure first.
Usually, the metadata is converted into a tabular format to allow the use of data analysis tools, such as [pandas](https://pandas.pydata.org/), or the geographical extension, [geopandas](https://geopandas.org/en/stable/).

### Pre-converted metadata
Instead of re-writing another parsing script, we recommend to use [](ben_gdf_builder:intro).
This library parses the all JSON files from the archive and converts them to a common geopandas parquet file.
See [](ben_gdf_builder:intro) for more information.

Do make it simpler to do statistical analysis, we provide pre-converted files.
These files (and the links) may change in the future!

- BigEarthNet-S2
   - [raw_ben_gdf.parquet](https://tubcloud.tu-berlin.de/s/gxp8KGk8TfcH6rR)
      - The original parquet file that is produced by parsing all metadata files and projecting to a common CRS
   - [extended_ben_gdf.parquet](https://tubcloud.tu-berlin.de/s/5cstd7EJRB8kCyL)
      - An extended version of the `raw_ben_gdf.parquet` file with additional metadata:
        - 19-class nomenclature
        - Covered by seasonal snow
        - Covered by clouds or shadows
        - Original split
        - Country
        - Season
   - [final_ben.parquet](https://tubcloud.tu-berlin.de/s/wtqZQKawLaBZZY8)
     - The recommended subset of `extended_ben_gdf.parquet`, where no patch is covered by snow, clouds or shadows and every patch has at least one target label in the 19-class nomenclature

#### Example output

<!-- :::{dropdown} BigEarthNet-S2-Example Metadata in tabular form
:::{glue:} ben-s2-gdf
::: -->

```{code-cell} ipython3
:tags: []

# scroll-output
from bigearthnet_gdf_builder.builder import get_gdf_from_s2_patch_dir

# gdf_builder also has a CLI tool to convert the entire archive into a single
# parquet file!
# Example "raw" subset
gdf = get_gdf_from_s2_patch_dir(ben_s2_path)
# showing first row as tables have display issues
gdf
```

Parquet files allow for easy data-processing and visualization.
These files work particularly well with geopandas:

```{code-cell} ipython3
# remove-input
gdf[
    gdf["name"].isin(
        ["S2B_MSIL2A_20170924T93020_69_24", "S2B_MSIL2A_20180204T94161_57_38"]
    )
].explore()
```

```{code-cell} ipython3
:tags: []

# scroll-output
from bigearthnet_gdf_builder.builder import add_full_ben_s2_metadata

# also provides a quick way to add important metadata
# example "metadata" subset
meta_gdf = add_full_ben_s2_metadata(gdf)
# showing first row as tables have display issues
meta_gdf
```

+++ {"tags": []}

:::{important}
Instead of writing another metadata loading script:
- Download one of the pre-converted files or
- Use the [](ben_gdf_builder:intro) tool to convert the metadata into a tabular format

:::

```{code-cell} ipython3
:tags: []


```
