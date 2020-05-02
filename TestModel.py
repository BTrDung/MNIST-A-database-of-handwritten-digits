from tensorflow.keras.models import load_model
from DataTraining import train_images, train_labels
from DataTesting import test_images, test_labels
model = load_model("main.h5")

print(model.metrics_names)
print(model.evaluate(train_images, train_labels, verbose=2))
print(model.evaluate(test_images, test_labels, verbose=2))
