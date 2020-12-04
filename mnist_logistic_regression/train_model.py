from load_data_train import train_images, train_labels
from logistic import train_by_logistic
from count_category import count
from wf import write_2D_to_file


def fix_label(category, y):
    n = len(y)
    arr = []
    for index in range(0, n):
        arr.append(y[index] == category)
    return arr


def train_model(train_images, train_labels):
    print('Training model.')
    weights = [[0 for _ in range(0, len(train_images[0]))] for i in range(0, 10)]

    for cate in range(0, 10):
        print('Training class ', cate)
        print('Fix label   -- ', end='')
        y = fix_label(int(cate), train_labels)
        x = train_images
        print('Done.')
        print('Train class -- ', end='')
        weights[cate] = train_by_logistic(x, y, weights[cate], iter=1500, alpha=0.5)

    write_2D_to_file(weights)
