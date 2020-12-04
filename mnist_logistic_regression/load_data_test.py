from load_img import test_images, test_labels
import numpy as np


def reshape(data):
    result = []
    count_pic = 0
    percent = 0
    for picture in data:
        count_pic += 1
        if count_pic % 2000 == 0:
            percent += 20
            print('percent:', percent, '%', '\t pic:', count_pic)
        arr = np.concatenate((np.reshape(np.array([np.array(i) for i in picture]), -1), [0]), None)
        result.append(arr)
    return result


print('Loading data test.')
test_images = test_images / 225
test_images = reshape(test_images)
print('-->Success!')
