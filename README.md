# PyTorch 101: building a model step-by-step

Learn the basics of building a PyTorch model using a structured, incremental and from first principles approach. Find out why PyTorch is the fastest growing Deep Learning framework and how to make use of its capabilities: autograd, dynamic computation graph, model classes, data loaders and more.

The main goal of this session is to show you how PyTorch works: we will start with a simple and familiar example in Numpy and "torch" it! At the end of it, you should be able to understand PyTorch's key components and how to assemble them together into a working model.

We will use Google Colab and work our way together into building a complete model in PyTorch. You should be comfortable using Jupyter notebooks, Numpy and, preferably, object oriented programming.

Open it in Google Colab [PyTorch101_Colab.ipynb](https://colab.research.google.com/github/dvgodoy/PyTorch101_ODSC_Europe2020/blob/master/PyTorch101_Colab.ipynb).

If you'd rather use a local environment, please follow these steps (assuming you use Anaconda):

- Install GraphViz: https://www.graphviz.org/

- Create a conda environment: `conda create -n pytorch101 pip conda python==3.6.8`

- Activate the conda environment: `conda activate pytorch101`

- Install PyTorch: https://pytorch.org/get-started/locally/

- Install other packages: `conda install scikit-learn==0.21.3 matplotlib==3.1.1 jupyter==1.0.0 ipywidgets==7.5.1 plotly==4.1.1 -c anaconda`

- Install torchviz: `pip install torchviz`

- Clone this repo: `git clone https://github.com/dvgodoy/PyTorch101_ODSC_Europe2020.git`

- Start Jupyter: `jupyter notebook`
