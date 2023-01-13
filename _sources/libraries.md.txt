# Helpful Libraries

:::{warning}
These libraries should be considered as experimental!

If you find any issues please use the official bug-tracker!
:::

The following is a short list of _unofficial_ BigEarthNet-related libraries:
## {{ BenCommon }}

The {{ BenCommon }} library provides a collection of high-level tools to better work with the BigEarthNet dataset.
Use this library to:
- Use any BigEarthNet related constants
    - Quickly print constants by using a CLI tool
- Safely read JSON files
- Deterministically multi-hot encode/decode 19/43-class labels
- Quickly accessing metadata from a patch for filtering
    - Country
    - Season
    - Original Split
    - If it is a _snowy_ patch
    - If it is a _cloudy/shadowy_ patch
    - Access related S1 or S2 patch
- Create CSV sets via a CLI tool
- Access example data without having to download the entire BigEarthNet archive

See the {{ BenCommon }} documentation for more details.

## {{ BenGdfBuilder }}
The {{ BenGdfBuilder }} library helps to generate and extend BigEarthNet GeoDataFrame’s.
Use this library to:
- Convert all the individual JSON files to a common tabular data structure
- Easy processing of metadata with GeoDataFrame's
    - Assign patches to country
    - Assign patches to season
    - Assign patches to original split
- Easy processing of the geographical information
- Create complex subsets
- In-depth statistichal analysis of the meta-data

See the {{ BenGdfBuilder }} documentation for more details.

## {{ BenInterface }}
The {{ BenInterface }} is a deep-learning agnostic wrapper for BigEarthNet patches.
The main use is to convert the patches to this intermediate format before processing it to a deep-learning specialized format.
Internally, the bands as stored as simple NumPy arrays.
The interface is very strict during the object creation to ensure that errors in the pipeline are catched early on.
It also provides introspection to quickly understand the underlying data structure.

See the {{ BenInterface }} documentation for more details.

## {{ BenEncoder }}
The goal of the {{ BenEncoder }} library is to quickly transform the original BigEarthNet archive into a deep-learning optimized format.
The long-term goal is to support multiple output formats.
As of now, the only supported target format is the LMDB archive format.

See the {{ BenEncoder }} documentation for more details.
