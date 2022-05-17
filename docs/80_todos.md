# ToDo

Here is a short collection of possible enhancements that could be done in the future:
- Write how BigEarthNet was created
    - What cloud/shadowy patches mean
    - What current issues are with the labels
    - Some documentation about the outlier regions
- Add information about Sentinel-1
    - Time difference between Sentinel-1/2
- Show example training process:
    - Read from LMDB file to get Interface
    - Interpolate necessary bands and stack them
    - Convert labels to multi-hot encoded
        - Why it is necessary to multi-hot encode dynamically (portugal labels)
- Extend {{ BenEncoder }} to show-case how to read from LMDB file
    - No interpolation/deep-learning related code!
- An in-depth discussion about possible subsets
    - Issues with multi-class (re-)sampling/balancing
    - General issues of different domains and translation of one result to the next
