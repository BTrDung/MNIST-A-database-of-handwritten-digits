import numpy as np
import time


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def train_by_logistic(x, y, w, iter, alpha):
    start_time = time.time()
    X = np.array([np.array(i) for i in x])
    Y = np.array(y)
    W = np.array(w)

    for i in range(0, iter):
        W = W + alpha * np.dot(Y.T - sigmoid(np.dot(X, W.T)), X) / len(y)

    print('Done.')
    end_time = time.time()
    print('Time to complete: ', end_time - start_time,' seconds')

    return W.tolist()
