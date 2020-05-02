from Data import train_images, train_labels

train_images = train_images / 225
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)

