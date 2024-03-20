## ZebraPose fork of ViTPose

The [project website](https://zebrapose.is.tue.mpg.de/) contains all the data and additional information.

You can find all the modified files in ZebraPose folder.
Those include:
1. New validation files for the ap10k dataset, which is the main configuration used in the ZebraPose work. Those will now print PCK at three different threshold and the parts pck as well.
2. New config files for the synthetic and mixed datasets. Those are in the config folder and are available for testing, trian from scratch and train with a pretrained backbone. Please note that you will have to change paths and jsons in those files according to your naming/saving
3. Edits in the `tools/` files, including a minor change in `model_split.py`
4. Some additional scripts to automatically get and process the results, and get a pandas dataframe in output


Please copy all of them in the main folder.

To install ViTPose follow the README_ViT.md instructions. 

### License
By using this code you agree to the [license terms](https://zebrapose.is.tue.mpg.de/license.html)

### Citation
If you use this software, please cite 

```
@INPROCEEDINGS{10256293,
  author={Bonetto, Elia and Ahmad, Aamir},
  booktitle={2023 European Conference on Mobile Robots (ECMR)}, 
  title={Synthetic Data-Based Detection of Zebras in Drone Imagery}, 
  year={2023},
  volume={},
  number={},
  pages={1-8},
  doi={10.1109/ECMR59166.2023.10256293}}
```

```
@misc{bonetto2023grade,
            doi = {10.48550/ARXIV.2303.04466},
            url = {https://arxiv.org/abs/2303.04466},
            author = {Bonetto, Elia and Xu, Chenghao and Ahmad, Aamir},
            title = {GRADE: Generating Realistic Animated Dynamic Environments for Robotics Research},
            publisher = {arXiv},
            year = {2023},
            copyright = {arXiv.org perpetual, non-exclusive license}
}
```
