# BEN On-Boarding Roadmap

We should share our expertise with BigEarthNet!

## What is the dataset about?

Give a general introduction to the multi-spectral data (comparable to my blog post).

- Where does the data come from?
- What is the purpose of the different bands?
- How do the images look like?
- Why do the images have a different spatial resolution?

## How do the statistics look like?

Give everyone an easy tool to calculate various statistics:
- Provide data in a standard tabular format (CSV) for initial exploratory analysis
    - Allow students to use the tools of their choice
    - Extra information should be **reproducible** (how were the patches assigned to a country, for example)
- Provide data with geometry information for more complex tasks (parquet format)
    - Allow code-use with zero installation overhead by providing Colab notebooks
    - Show recommended ways to work with the geographic information
- Include 19-label information

## How do I load the data and visualize the results?

We should give a top-down approach!

1. Show how to load/work with the provided TIFF files
    - Give a little background information about the interpolation step
        - **Extremely** important for reproducibility
2. **Stress** the issues one can have when working with `rasterio/gdal/cartopy` library
3. Lead to the next section, where we show how to work _efficiently_ with the data

I would even recommend setting up another online tool for quick visualization.
In case somebody wants to retrieve some basic information about a specific patch,
we could draw the each band, show the location of the patch and the corresponding labels.

## How do I efficiently load the data?

To **greatly** reduce training time and power consumption, give a detailed overview on how we can convert the data into a better representation for Deep Learning purposes.

For example:
- Directly loading via TIFF files is extremely slow
- More optimized variants allow for up to 20-40x faster data loading!
  - One researcher, for example, loaded directly via TIFF and resulted in comparatively long training times (at least 2/3x slower)
- Explain the normalization step in more detail
  - Explain where it comes from

By openly disclosing this investigation, we can help others not unnecessarily waste energy and compute time.

## How does the geographic distribution look like?

- Partially solved by BEN Portal
- Could also provide a different optimized platform to show label distributions on a country scale.
    - Mostly useful to get a "better feel" of the data

## What subset should I use?

We could have two subsets:

1. Serbia Summer
2. Representative Subset

Both datasets should be reproducible and have a **Leaderboard**.

The leaderboard should help everyone that is developing a new method.
When we accumulate the scores into a single source, it will be a lot easier to find bugs from an earlier stage and to get an initial feel for the performance.
There would be multiple leaderboard scores (IR, multi-class classifications) with various metrics but combined into a single table.

Furthermore, these datasets should be provided in the correct format, to allow for a quick transition from the subset to the entire BEN dataset.

- Could also provide two/three extra random splits for stability tests
  - It is easy to reproduce, but then again, we have the results on a single score

# Goals

- Lowers the entry barrier for new researchers, especially from other domains
- Helps to further
