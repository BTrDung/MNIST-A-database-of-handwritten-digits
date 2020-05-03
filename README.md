# MNIST

## Introduction
MNIST is a database of handwritten digits available on http://yann.lecun.com/exdb/mnist. The digits have been size-normalized and centered in a fixed-size image.

There are 4 files:
```
train-images-idx3-ubyte: training set images
train-labels-idx1-ubyte: training set labels
t10k-images-idx3-ubyte:  test set images
t10k-labels-idx1-ubyte:  test set labels
```
The training set contains 60000 examples, and the test set 10000 examples.

In this project, i will use a convolutional neural network for handwritten digit classification from scratch.

Accuracy persent was tested on training set ![GitHub ACWithDataTraining](https://img.shields.io/badge/accuracy-99.65%25-blue)

Accuracy persent was tested on testing set ![GitHub ACWithDataTesting](https://img.shields.io/badge/accuracy-98.71%25-blue)

Read more about MNIST on Wikipedia: https://en.wikipedia.org/wiki/MNIST_database.

## Requirements

Use Python 3. 

This project used Python version 3.8.2 and Pycharm with Anaconda environment to run. 

You can download Python and Pycharm by following links: 

Python: https://www.python.org/downloads/

Pycharm: https://www.jetbrains.com/pycharm/

## Installation

Clone/ download my git: https://www.anaconda.com/

Open folder ```.vscode -> tasks.json ```. 

Copy your Python.exe location (where you have installed Python) and paste to Line 12.

Example: My Python location is ```C:\Users\ABC\AppData\Local\Programs\Python\Python38\python.exe```. Copy link location and paste into
```tasks.json``` with a little changes like this:
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "RUN Python File",
            "type": "shell",
            "command": [
                "C:\\Users\\ABC\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
                ,"-u",
                "${file}"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            },
            "problemMatcher": []
        }
    ]
}
```

Do the same thing with ```settings.json```: 
```
{
    "python.pythonPath": "C:\\Users\\ABC\\AppData\\Local\\Programs\\Python\\Python38\\python.exe"
}
```

Use Visual Studio Code to open project. Use terminal and get package: 
```
pip install python-mnist
```

```
pip install scikit-learn
```

Press F5 and choose Python to see what it can do. 
