import PIL
import collections
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.layers import Convolution2D, MaxPooling2D, Flatten, Dense

print("Load data")
mnist = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images / 225
# [0, 1]
test_images = test_images / 225
# [0, 1]

train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

print("Complete")

model = tf.keras.Sequential()
# (28x28x1)
model.add(Convolution2D(filters=6, kernel_size=(5, 5), activation='relu', input_shape=(28, 28, 1)))
# (24x24x6)
model.add(MaxPooling2D(pool_size=(2, 2)))
# (12x12x6)
model.add(Convolution2D(filters=16, kernel_size=(5, 5), activation='relu'))
# (8x8x16)
model.add(MaxPooling2D(pool_size=(2, 2)))
# (4x4x16)
model.add(Flatten())
# 1D
model.add(Dense(128, activation='relu'))
model.add(Dense(84, activation='relu'))
model.add(Dense(10, activation=tf.nn.softmax))

model.summary()
# training

print("Train")
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
history = model.fit(train_images, train_labels, batch_size=32, validation_split=0.2, epochs=3, verbose=1)
print("Training complete")

model.save("TestModel. h5")
