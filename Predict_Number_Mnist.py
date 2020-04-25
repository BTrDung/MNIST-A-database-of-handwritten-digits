import PIL
import os
import collections
import numpy as np
import tensorflow as tf
import imageio
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

model = load_model("TestMyModel.h5")
Test_images = LoadIMG = imageio.imread("_________________")
Test_images = Test_images.reshape(1, 28, 28, 1)
Test_images = Test_images / 225
predict_number = model.predict(Test_images)
print(predict_number.argmax())
