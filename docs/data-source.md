# Data Source

[BigEarthNet](bigearth.net) contains 590,326 pairs of Sentinel-1 and Sentinel-2 image patches.
Two datasets belong to the BigEarthNet collection:

- BigEarthNet-S2 ({{ben}} with Sentinel-2 image patches)
- BigEarthNet-S1 ({{ben}} wiht Sentinel-1 image patches)

BigEarthNet-S2, initially named BigEarthNet, was released first.
After adding the BigEarthNet-S1 archive, the term _BigEarthNet_ has become an umbrella term for both datasets.

:::{note}
If both are used in a multi-modal fashion, the _combined_ dataset
is called _BigEarthNet-MM_.
So when referring to _BigEarthNet-MM_ it technically refers to separate
dataset _files_.
:::

:::{important}
Due to historical reasons, BigEarthNet and BigEarthNet-S2 are often used interchangeably.
:::

The images cover ten different European countries that were acquired from June 2017 to May 2018,
with the goal to acquire all the chosen locations in different seasons[^seasons].

[^seasons]: Due to restrictions of finding tiles with a low cloud cover percentage, this has not been
possible at every location in the given time span.

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
Sentinel-2 is a high-resolution, multispectral imaging mission from the European Union's [Copernicus Program](https://www.copernicus.eu/en) for Earth observation.
The Sentinel-2 mission is based on a constellation of two identical satellites (Sentinel-2A and Sentinel-2B) in the same orbit.
Each satellite has a [Multi-Spectral Instrument (MSI)](https://sentinel.esa.int/web/sentinel/missions/sentinel-2/instrument-payload)
that samples 13 spectral bands (four bands at 10m, six bands at 20m and three bands at 60m spatial resolution) with a high
revisit time (10 days at the equator with one satellite, and 5 days with 2 satellites under cloud-free conditions which results
in 2--3 days at mid-latitues).
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

The 10m spatial resolution bands B04, B03, and B02 are the red, green, and blue (RGB) channels.
The last 10m resolution band, B08, covers a broader spectrum than B08A but is less resistant against water vapor contaminating the spectral reflectance.
As some applications suffer from possible contamination, the narrower, lower spatial resolution band B08A was added.
To cover all use-cases, both bands were included, even if they overlap in the sensed spectrums {cite:p}`sentinel_band_heritage`.
Concatenating these spectrums results in images with twelve channels.

:::{important}
- BigEarthNet-S2 dropped channel B10 from the original Sentinel-2 data, as the band does not contain surface-level information. (Or more specifically, B10 is dropped
during the BOA calculation with the `sen2cor` tool.)
- The bands B08 and B8A are included, even if they overlap in the sensed spectral reflectivity.
  - Allows the user to decide how to handle the overlap. Refer to Sentinel-2 Heritage document {cite:p}`sentinel_band_heritage` for more details.
:::

For a more detailed overview of the Sentinel-2 mission, please take a look:
- The [official Sentinel-2 website](https://sentinel.esa.int/web/sentinel/missions/sentinel-2)
- The [Sentinel-2 User Handbook](https://sentinel.esa.int/documents/247904/685211/Sentinel-2_User_Handbook)
- At the [Sentinel-2 ESA’s Optical High-Resolution Mission for GMES Operational Services](https://esamultimedia.esa.int/multimedia/publications/SP-1322_2/offline/download.pdf) {cite:p}`Fletcher2012`

## Sentinel-1

:::{admonition} ToDo
:class: todo

Add some information about Sentinel-1
:::
