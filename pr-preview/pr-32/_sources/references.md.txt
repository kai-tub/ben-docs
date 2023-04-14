# Further references

Here, we provide a collection of relevant links provided by our research group:

- The first BigEarthNet (S2) paper {cite:t}`BEN`
- The BigEarthNet-MM publication + the recommended 19-class nomenclature {cite:t}`BEN19labels`

## Pretrained models
Every repository includes code to re-run the training procedure.
These models are all trained with the TensorFlow library.

- Pretrained models trained on BigEarthNet-S2 with 43-classes
    - https://git.tu-berlin.de/rsim/BigEarthNet-S2_43-classes_models
- Pretrained models trained on BigEarthNet-S2 with 19-classes
    - https://git.tu-berlin.de/rsim/BigEarthNet-S2_19-classes_models
- Pretrained multi-modal models trained on BigEarthNet-S1 and BigEarthNet-S2 simultaneously
    - https://git.tu-berlin.de/rsim/BigEarthNet-MM_19-classes_models

## BigEarthNet Tools
- BigEarthNet-S1 Tools
  - https://git.tu-berlin.de/rsim/BigEarthNet-S1_tools
  - Read GeoTIFF patches from BigEarthNet-S1
  - Script to extract names and download links of the Sentinel-1 Level-1C GRD tiles
    - Requires the BigEarthNet-S1 dataset on disk
- BigEarthNet-S2 Tools
  - https://git.tu-berlin.de/rsim/BigEarthNet-S2_tools
  - Read GeoTIFF patches from BigEarthNet-S2
    - While skipping cloudy/snowy patches
  - Script to extract names and download links of the Sentinel-2 Level-1C tiles
    - Requires the BigEarthNet-S2 archive on disk
- Code to read pairs of Sentinel-1 and Sentinel-2 patches
    - https://git.tu-berlin.de/rsim/BigEarthNet-MM_tools

## Bibliography

```{bibliography}
  :style: plain

```

