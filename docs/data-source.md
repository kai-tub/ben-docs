# Data Source

[BigEarthNet](bigearth.net) is a collection of satellite images primarily designed to train machine-learning models.

Two datasets belong to the BigEarthNet collection:
- BigEarthNet-S2
- BigEarthNet-S1

BigEarthNet-S2, initially named BigEarthNet, was released first.
After adding the BigEarthNet-S1 archive, the term _BigEarthNet_ has become an umbrella term for both datasets.

The difference between these two archives is the data _source_.
Both archives _sensed_ the same regions, but the images were taken from different satellites.
The S2 archive used the Sentinel-2 satellites and S1, the satellite of the Sentinel-1 mission. Hence, the name S1/2 for Sentinel-1/2.

:::{important}
Due to historical reasons, BigEarthNet and BigEarthNet-S2 are often used interchangeably.
:::

The images cover ten different European countries that were sensed (multiple times) from June 2017 to May 2018.

:::{dropdown} Sensed Countries
- Austria
- Belgium
- Finland
- Ireland
- Kosovo
- Lithuania
- Luxembourg
- Portugal
- Serbia
- Switzerland
:::

## Sentinel-2
The Sentinel-2 mission is a multi-spectral high-resolution earth monitoring mission from the European Union's earth observation program [Copernicus Program](https://www.copernicus.eu/en).
The Sentinel-2 mission consists of two polar-orbiting satellites, Sentinel-2A and Sentinel-2B, with a high revisit time (5 -- 10 days).
Each satellite has a [Multi-Spectral Instrument (MSI)](https://sentinel.esa.int/web/sentinel/missions/sentinel-2/instrument-payload) that senses 13 different spectrums of light with varying spatial resolution.
The following [figure](sentinel2-bands) visualizes the spectrum of each band grouped by their spatial resolution.

```{figure-md} sentinel2-bands
<img src="images/ben_bands_vis.*" alt="BigEarthNet Bands" class="bg-primary mb-1" width="90%">

Sentinel-2 bands grouped by spatial resolution
```

The spectrums range from visible (380nm–700nm), near-infrared (700nm–1100nm) to short-wave infrared (1100nm–3000nm) light.
The low-spatial resolution 60m bands are designed for aerosol (B01), water-vapor (B09), and cirrus cloud (B10) detection.

BigEarthNet does not include band B10 as B10 provides no surface-level information {cite:p}`cirrus`.
Band B10 is dropped after converting a Sentinel-2 L1C data product, which encodes the TOA, to a Sentinel-2 L2A product containing the BOA data.
See the official [Sentinel-2 data products page](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2/data-products) for more information.

The 20m bands in the near-infrared range (B05, B06, B07, B8A) are vital for differentiating vegetation from other objects.
The remaining 20m bands in the short-wave infrared spectrum (B11, B12) are helpful for snow, ice, and cloud discrimination {cite:p}`Fletcher2012`.

The high spatial resolution bands B04, B03, and B02 are the classic red, green, and blue (RGB) channels.
The last 10m resolution band, B08, covers a broader spectrum than B08A but is less resistant against water vapor contaminating the spectral reflectance.
As some applications suffer from possible contamination, the narrower, lower spatial resolution band B08A was added.
To cover all use-cases, both bands were included, even if they overlap in the sensed spectrums {cite:p}`sentinel_band_heritage`.
Concatenating these spectrums results in images with twelve channels, compared to the more common three RGB channels.

:::{important}
- BigEarthNet-S2 dropped channel B10 from the original Sentinel-2 data, as the band does not contain surface-level information.
- The bands B08 and B8A are included, even if they overlap in the sensed spectral reflectivity.
  - Allows the user to decide how to handle the overlap.
:::

## Sentinel-1

:::{admonition} ToDo
:class: todo

Add some information about Sentinel-1
:::
