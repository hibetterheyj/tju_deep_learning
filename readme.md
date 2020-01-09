### Course repo for *Deep learning@Tongji Univ.* (Elective Course)

### 同济大学 - 深度学习（选修）

Final project and four assignments as of 20.01.09, respectively

#### Course info

Supervised by Professor, [Yin Wang](http://web.eecs.umich.edu/~yinw/)

- Python basics
- Linear regression & Logistic regression
- NN basics
- Convolutional neural network
- Object detection
- Style transfer
- etc.

---

#### Final Project

> Enhanced 3D Zonal Segmentation of the Prostate on MRI via Enhanced Weight-Standardization and Group-Normalization
>
> 基于的Weight-Standardization和Group-Normalization在前列腺MRI数据集上的三维区块分割

In this final project, I utilized Weight Standardization (WS) as well as GroupNorm to accelerate neural networks training and improve overall segmentation results for 3D Zonal Segmentation of the Prostate on MRI images. WS is targeted at the micro-batch training setting where each GPU typically has only 1-2 images for training. The quantitative experiments have shown that UWG-Net can outperform the performances of 3D U-Net (baseline) with BN trained with small batch sizes with only two more lines of code. The effectiveness of WS is verified on the open-source Prostate Dataset, including 22 training cases and 10 testing cases. 

---

#### Assignments

Using [nbviewer](https://nbviewer.jupyter.org/) for better and faster rendering!

- (1) Linear & (2) Logistic (multiple binary classifiers method) regression

[[notebook1](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%231/assignment1.1.ipynb)], [[notebook2](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%231/assignment1.2.ipynb)]

- (1) Logistic (softmax method) regression & (2) Fully connected neural network

[[notebook1](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%232/softmax-mnist.ipynb)], [[notebook2](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%232/shallownn-mnist-torch.ipynb)]

- Convolutional neural network implemented via (1) PyTorch & (2) Fastai

[[notebook1](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%233/cifar-cnn.ipynb)], [[notebook2](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%233/CIFAR-Fastai.ipynb)]

- Re-implemented one style transfer algorithm (MSG-Net) via PyTorch

[[notebook](https://nbviewer.jupyter.org/github/hibetterheyj/tju_deep_learning/blob/master/assignment/%234/HYJ-Minimum-Pack/He-Yujie-msgnet.ipynb)]

Weekly solution and codes are available in `*.ipynb`. Best wishes!

每周解答和代码具体可见`*.ipynb`。祝好！

#### Others

For other solution, you can refer to :thumbsup: [ShallowDock/DLcourse](https://github.com/ShallowDock/DLcourse ) 