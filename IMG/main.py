from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from mnist import MNIST

train_limit = 50000
test_limit = 500

print("Load dataset")

mndata = MNIST(".")

train_images, train_labels = mndata.load_training()
test_images, test_labels  = mndata.load_testing()

train_labels = train_labels.tolist()
test_labels = test_labels.tolist()

print("Training")
clf = KNeighborsClassifier()
clf.fit(train_images[:train_limit], train_labels[:train_limit])

print("Testing")
predicted = clf.predict(test_images[:test_limit])

print("Score: ", accuracy_score(test_labels[:test_limit], predicted))
