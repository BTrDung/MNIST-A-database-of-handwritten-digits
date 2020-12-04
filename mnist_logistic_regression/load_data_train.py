from load_img import train_images, train_labels
import numpy as np


def reshape(data):
    result = []
    count_pic = 0
    percent = 0
    for picture in data:
        count_pic += 1
        if count_pic % 12000 == 0:
            percent += 20
            print('percent:', percent, '%', '\t pic:', count_pic)

        arr = np.concatenate((np.reshape(np.array([np.array(i) for i in picture]), -1), [0]), None)
        result.append(arr)
    return result


print('Loading data train.')
train_images = train_images / 225
train_images = reshape(train_images)
print('-->Success!')
