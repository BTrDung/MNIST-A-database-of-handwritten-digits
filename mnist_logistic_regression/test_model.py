import numpy as np


def make_list(w):
    list_w = list(w[0].split(" "))
    arr = []
    for i in list_w:
        if i != '':
            arr.append(float(i))
    return arr


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def predict_label(img, w):
    result = 0
    max_percent = 0.000000000
    for cate in range(0, 10):
        array = np.array(w[cate])
        image = np.array(img)
        f = np.dot(array, image.T)
        sg = sigmoid(f)
        if sg > max_percent:
            max_percent = sg
            result = cate

    return result


def test_model(test_img, test_lab, w):
    count_correct = 0
    count_process = 0
    percent = 0
    weights = [make_list(w[cate]) for cate in range(0, 10)]
    for index in range(0, len(test_img)):
        img = test_img[index]
        lab = test_lab[index]

        predict = predict_label(img, weights)

        count_process += 1
        count_correct += (predict == lab)

        if count_process % (len(test_img) // 10) == 0:
            percent += 10
            print('Process: ',percent,'%, \t Pictures: ', count_process,' \t  Correct:', count_correct)

    print('Number of correct answer:', count_correct)
    print('Accuracy: ', count_correct / len(test_img) * 100,'%')

