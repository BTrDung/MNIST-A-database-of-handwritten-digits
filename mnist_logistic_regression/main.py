from load_data_train import train_images, train_labels
from load_data_test import test_images, test_labels
from load_parameters import update_parameters
from train_model import train_model
from test_model import test_model

train_model(train_images, train_labels)

weights = update_parameters()

print('Test model with data train.')
test_model(train_images, train_labels, weights)

print('Test model with data test.')
test_model(test_images, test_labels, weights)
