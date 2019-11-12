### Assignment #4 Readme

- Environment install **(you can install in commend line)**

open cmd or terminal and input as follows:

```
conda create -n py35torch40 python=3.5
conda activate py35torch40
conda install pytorch=0.4.0 torchvision cuda80 -c pytorch
conda install jupyterlab
# running camera_demo.py
conda install opencv
pip install torchfile
cd <experiments-folder>
python camera_demo.py demo --model models/21styles.model
```

encounter `ImportError: No module named 'win32api'`, you can input as follows:

```shell
pip install pypiwin32
```

- Generate `requirements.txt`

As the comment at the top indicates, the output of

```
conda list -e > requirements.txt
```

- Use `requirements.txt`

can be used to create a `conda` virtual environment with  **(you can also install with txt-file)**

```
conda create --name  --file requirements.txt
```

- For more details
  1. Source repo: **[zhanghang1989/PyTorch-Multi-Style-Transfer](https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer)**
  2. Environments use: [From conda create requirements.txt for pip3](https://stackoverflow.com/questions/50777849/from-conda-create-requirements-txt-for-pip3 )
    