## Tongji Univ. Deep Learning Final Project | 深度学习期末项目

#### Enhanced 3D Zonal Segmentation of the Prostate on MRI via Enhanced Weight-Standardization and Group-Normalization

#### 基于的Weight-Standardization和Group-Normalization在前列腺MRI数据集上的三维区块分割

#### Author

Yujie He，何宇杰

#### Abstract

In this final project, I utilized Weight Standardization (WS) as well as GroupNorm to accelerate neural networks training and improve overall segmentation results for 3D Zonal Segmentation of the Prostate on MRI images. WS is targeted at the micro-batch training setting where each GPU typically has only 1-2 images for training. The quantitative experiments have shown that UWG-Net can outperform the performances of 3D U-Net (baseline) with BN trained with small batch sizes with only two more lines of code. The effectiveness of WS is verified on the open-source Prostate Dataset, including 22 training cases and 10 testing cases. 



2020.01.08