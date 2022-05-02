# Problem statement

I've talked with colleagues about their experience working with BigEarthNet and their problems during their time working with the archive.
I've also asked master thesis students what topics seem hard to grasp from an _outside_ perspective.
Some of these problems were also mentioned in the intermediate presentation and during discussions with the VQA project group.

The most common issues are:
- Many new terms are introduced without giving a short introduction (multi-spectral/satellite terminology, CLC, 43- vs. 19-class nomenclature, etc.)
- Hard to perform statistical analysis
    - Especially when trying to use geographical information
    - Code is often duplicated as there is no _general_ code to convert the raw metadata to a tabular format
    - No public tabular format of the BigEarthNet archives
- Visualization of true-color images and individual bands is not obvious
- Efficient data-loading of BigEarthNet patches to reduce training time is often unclear
    - The raw GeoTIFF files are often loaded, which is at least 5x slower than a more DL-specific data structure
- No _official_ recommended subset for initial experiments
    - Internally, we often use Serbia, but the list of patches is not publicly available
    - Work done on the subset is sometimes hard to compare to work from other researches as there is no internal _score-board_
- Information about BigEarthNet is distributed across different repositories and papers

Tom's work on the public [BigEarthNet Starter-Kit](https://git.tu-berlin.de/rsim/starter-kit-bigearthnet/-/tree/main) goes in the right direction, but is not ideal from the perspective of a student or an outside researcher for the following reasons:
- Requires access to the `erde` server, as the data is assumed to be in a pre-converted state
	- `HDF5` file to access metadata with a size of 215GB
	- `lmdb` file for training with a size of 168GB
- No reference on how to generate the `lmdb` nor the `HDF5` archive
	- What happens if the data is lost?
- Files are too large to distribute efficiently and to let students perform quick statistical analysis

There is still a need for tabular data to perform statistical analysis.
The pipeline to generate the tabular data should be accessible and easily re-create the results from the raw archive.
There is also a need for a guide to convert the raw BigEarthNet data to a deep-learning structure to train deep neural networks efficiently.
