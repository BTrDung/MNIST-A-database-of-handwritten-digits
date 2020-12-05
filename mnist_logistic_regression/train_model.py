from load_data_train import train_images, train_labels
from logistic import train_by_logistic
from count_category import count
from wf import write_2D_to_file


def fix(cate, x, y):
    img = x
    lab = [(y[index] == cate) for index in range(0, len(y))]
    return img, lab


def train_model(train_images, train_labels):
    print('Training model.')
    weights = [[0 for _ in range(0, len(train_images[0]))] for i in range(0, 10)]

    for cate in range(0, 10):
        print('Training class ', cate)
        print('Fix label   -- ', end='')
        x, y = fix(cate, train_images, train_labels)
        print('Done.')
        print('Train class -- ', end='')
        weights[cate] = train_by_logistic(x, y, weights[cate], iter=2500, alpha=0.5)

    write_2D_to_file(weights)
