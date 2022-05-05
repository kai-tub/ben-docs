# Remote Sensing Basics
Before going into the details of {{ ben }}, the following section will give a short introduction to common terms of the remote sensing domain.

Spatial resolution
  : One important concept when working with remote sensing data is the spatial resolution of an image.
    The spatial resolution describes how _large_ a pixel is.
    A spatial resolution of 10m indicates that each pixel covers a region with a width and height of 10m.
    In other words, objects smaller than 10m² cannot be represented, as they are too small.

Spectral reflectance
  : When light hits a surface, the surface partially absorbs and reflects the incoming electromagnetic spectrum.
  The reflected electromagnetic spectrum is what an observer (our eyes or a satellite) perceives and processes.
  We perceive a green leaf as green, as the green spectrum is the largest reflected spectrum.

Band
  : A band is a predefined range of the electromagnetic spectrum.
    For example, the green band is often defined as the spectrum with a wavelength from 500 to 565 nanometers.

Tiles or Granules
  : When talking about satellite images, a _tile_ (also _granule_) often refers to predefined regions.
    The Sentinel-2 mission has defined 100km x 100km tiles that divides the earth into [60 unique zones](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/product-types).

Patches
  : Patches is used as a term to specify a valid _sub-image_ of a tile. "Patch" is not a standardized term, but in the BigEarthNet documentation, it refers to a 1200m x 1200m area of a Sentinel tile.

It is necessary to split a tile into multiple patches further because tiles are too large to be effectively used for machine learning.
For comparison, a single Sentinel-2 tile is ~800MB large, while a standard image size is around ~100kB.

:::{note}
The spatial resolution can differ between bands from the same satellite.
:::
