from load_data_train import train_images, train_labels


def count():
    print('Catetoring')
    num = len(train_images)
    category = [[] for i in range(0, 10)]

    for iter in range(0, num):
        picture = train_images[iter]
        labels = train_labels[iter]
        category[labels].append(picture)

    for iter in range(0, 10):
        print('Class ', iter, ': ', len(category[iter]), ' pictures.')
    print('-->Success')

