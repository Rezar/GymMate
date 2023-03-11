Ruizhi Ou (Melody)     *3/11/2023*
# About ViTPose

**ViTPose** is a *pose estimation* model that obtains state-of-the-art (SOTA) performance of 80.9 AP on the MS COCO Keypoint test-dev set.

**Paper**: *[ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation](https://arxiv.org/abs/2204.12484)* (Yufei Xu, Jing Zhang, Qiming Zhang Dacheng Tao).

**GitHub**:  https://github.com/ViTAE-Transformer/ViTPose


# Prerequisite to Running ViTPose

We are currently concentrating on running the model on **2D WholeBody Video** datasets, which includes models:

 - **ViTPose+ S** (S-small)
 - **ViTPose+ B** (B-big)
 - **ViTPose+ L** (L-large)
 - **ViTPose+ H** (H-huge-I suppose)

The models require the below prerequisites to run, please have them installed before running (if you haven't done so). Please install *in the following order*, since some serve as the prerequisites for others, and stick to the given versions.

All codes will be presented in the *ViTPose.ipynb* file in this folder.

You could install following the **versions** either in the "Author Suggested" or "Verified (run on these versions and succeeded)" column.
|                |Author Suggested               |Verified                      |
|----------------|-------------------------------|-----------------------------|
|Python          |3.8.10                         |3.8.x, 3.9.x, 3.10.x            |
|Conda           |No specific requirement        |23.1.0          |
|Torch         |1.9.0                          |1.9.1        |
|MMCV-full       |1.3.9                          |1.5.0           |
|CUDA            |11.3                           |11.8            |
|MMDet           |No specific requirement       |2.28.2         |

## 1. Python

The author run the model on version **3.8.10**.
It also worked on other versions such as **3.8.x**, **3.9.x** and **3.10.x**.

## 2. Conda

It worked on the latest version **23.1.0**.
You could either install the *full version*, or install the *lite version using Miniconda* then upgrade it.


## 3. Virtual Environment (optional)

It is not required, but always encouraged to work in a virtual environment, if you haven't done so.

## 4. Torch

The author run the model on version **1.9.0a0+c3d40fd**. *TorchVision* **0.10.0a0**.
The version verified is **1.9.1**, *TorchVision* **0.10.1**.

## 5. MIM

**MIM** ([GitHub](https://github.com/open-mmlab/mim)) provides a unified interface for launching and installing OpenMMLab projects and their extensions, and managing the OpenMMLab model zoo. Here are the instructions for [installation](https://github.com/open-mmlab/mim/blob/main/docs/en/installation.md).

Just follow the installation instructions. MIM is required to later install MMCV-full and MMDet.

## 6. MMCV-FULL

**MMCV** ([GitHub](https://github.com/open-mmlab/mmcv)) is a foundational library for computer vision research.

There are MMCV-full and MMCV (lite), please be sure to install **MMCV-full**.

The author run the model on version **1.3.9**.
The version verified is **1.5.0**.

## 7. CUDA

**CUDA** is a parallel computing platform and programming model developed by NVIDIA for general computing on graphical processing units (GPUs). It is required to run these models.

The below versions refer to the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit).

The author run the model on version **11.3**.
The version verified is **11.8**. It should work on all versions higher than 10.2.

## 8. MMDET (mmdetection)

**MMDET** ([GitHub](https://github.com/open-mmlab/mmdetection)) is for object detection.

*Prerequisites*: It requires Python 3.7+, CUDA 9.2+ and PyTorch 1.5+ (should all be met if you followed the abovementioned steps).

The author didn't specify a version.
The version verified is **2.28.2**. 

## 9. NVIDIA apex

I didn't really succeeded on this one. Good luck.

## 10. ViTPose

Be sure to install the same version as the MMCV-full you installed when running:
`git checkout v1.5.0`
