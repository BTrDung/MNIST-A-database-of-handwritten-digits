# MNIST - A database of handwritten digits 

## Introduction
MNIST is a database of handwritten digits available on http://yann.lecun.com/exdb/mnist. The digits have been size-normalized and centered in a fixed-size image.

There are 4 files:
You can use direct links to download the dataset.

| Name  | Content | Examples | Size | Link |
| --- | --- |--- | --- |--- |
| `train-images-idx3-ubyte.gz`  | training set images  | 60,000|9912422 bytes | [Download](http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz)|
| `train-labels-idx1-ubyte.gz`  | training set labels  |60,000|28881 bytes | [Download](http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz)|
| `t10k-images-idx3-ubyte.gz`  | test set images  | 10,000|1648877 bytes | [Download](http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz)|
| `t10k-labels-idx1-ubyte.gz`  | test set labels  | 10,000| 4542 bytes | [Download](http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz)|

The training set contains 60000 examples, and the test set 10000 examples.

In this project, i will use a convolutional neural network (CNN) for handwritten digit classification from scratch.

Accuracy persent was tested on training set 
![GitHub ACWithDataTraining](https://img.shields.io/badge/accuracy-99.65%25-blue)
![GitHub LSWithDataTraining](https://img.shields.io/badge/loss-0.0301-blue)

Accuracy persent was tested on testing set 
![GitHub ACWithDataTesting](https://img.shields.io/badge/accuracy-98.71%25-blue)
![GitHub LSWithDataTesting](https://img.shields.io/badge/loss-0.1373-blue)

Read more about MNIST on Wikipedia: https://en.wikipedia.org/wiki/MNIST_database.

## Requirements

Use Python 3. 

This project used Python version 3.7 and Pycharm with [Anaconda](https://www.anaconda.com/) environment to run. 

## Installation

Download my [git](https://github.com/BTrDung/MNIST.git) as a ZIP file: https://github.com/BTrDung/MNIST.git

Python: https://www.python.org/downloads/

Pycharm: https://www.jetbrains.com/pycharm/

Anaconda: https://docs.anaconda.com/anaconda/install/hashes/win-3-64/

## Instruction 

<details><summary>Install Anaconda</summary><p>
  
* After install Anaconda with *.ext, you can run this file and press ```Next```.
  
 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/1.png)

* Press ```Agree```.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/2.png)

* Choose ```Just me``` and press ```Next```.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/3.png)
 
* I press ```Next``` in this step.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/4.png)
 
* Press ```Install```.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/5.png)
 
* Wait until it finishes.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/6.png)
 
* Now, you done!. Press ```Next```.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/7.png)
</p></details><p></p>

<details><summary>Create project by Pycharm</summary><p>
  
* Open Pycharm.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/1.png)

* Create new project, ```File``` - ```New project...```.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/2.png)
 
* Create your project and choose ```New environmet using``` is Conda. 
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/3.png)

* After create your project, press ```ctrl + alt + s``` to see Project Interpreter. 
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/4.png)
 
* Open your project folder and extract the ZIP file that you downloaded from github.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/5.png)
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/6.png)
 
 * Open Pycharm, you will see all files have been extracted.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/7.png)
 
 * Open terminal, type ```pip install tensorflow``` and wait until it finishes downloading.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/8.png)
 
 If you see this line, you had install success tensorflow library.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/9.PNG)

* Open ```test model.py``` and press ```ctrl + shift + f10``` to run and see result.

 ![alt text](https://github.com/BTrDung/Complex/blob/master/CreProjMNIST/10.png)
</p></details><p></p>

