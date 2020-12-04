import tensorflow as tf

data = tf.keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data()

