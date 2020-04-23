from __future__ import division, print_function, unicode_literals
from mnist import MNIST
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, Flatten, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt

mndata = MNIST(".")
train_images, train_labels = mndata.load_training()
#test_images, test_labels = mndata.load_testing()
print("Load data success.")

New_train_images = train_images
New_train_labels = train_labels

New_train_images = train_images.reshape(60000, 28, 28, 1) / 255
New_train_labels = to_categorical(New_train_labels, 10)

myModel = Sequential()
myModel.add(Conv2D(32, kernel_size=(3, 3), activatiodn='relu', input_shape=(28, 28, 1)))
myModel.add(Conv2D(64, (3, 3), activation='relu'))
myModel.add(MaxPooling2D(pool_size=(2, 2)))
myModel.add(Dropout(0.25))
myModel.add(Flatten()) # flattened the data into a 1D array
myModel.add(Dense(128, activation='relu'))
myModel.add(Dropout(0.5))
myModel.add(Dense(10, activation='relu'))
