# MNIST

## Introduction
MNIST is a database of handwritten digits available on http://yann.lecun.com/exdb/mnist. The digits have been size-normalized and centered in a fixed-size image.

There are 4 files:
You can use direct links to download the dataset. The data is stored in the **same** format as the original [MNIST data](http://yann.lecun.com/exdb/mnist/).

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
 
* Wait until it finish.
 
 ![alt text](https://github.com/BTrDung/Complex/blob/master/InsAnaconda/6.png)
 
</p></details><p></p>
Step 2: Create your project by Pycharm with Conda environment. 

Step 3: Copy all the files which contained in the ZIP file after extracted into your project local.

Step 4: Open terminal, type ```pip install tensorflow``` and wait until it finishes downloading.

Step 5: Run file ```test model.py``` by ```ctrl + shift + f10``` and see result.
