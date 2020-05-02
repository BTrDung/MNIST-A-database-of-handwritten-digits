from Data import test_labels, test_images

test_images = test_images / 225
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
