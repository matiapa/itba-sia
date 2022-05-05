import gzip
import numpy as np
import sys
sys.path.append("..")
from container import *
import sklearn

def get_mnist_container():
    items_size = 30000
    train_size = 29500
    test_size = items_size - train_size
    f = gzip.open('../train-images-idx3-ubyte.gz','r')
    labels_f = gzip.open('../train-labels-idx1-ubyte.gz','r')
    labels = []

    labels_f.read(8)
    for i in range(0, items_size):   
        buf = labels_f.read(1)
        label = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
        labels.append(label)

    image_size = 28
    f.read(16)
    buf = f.read(image_size * image_size * items_size)
    data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
    data = data.reshape(items_size, image_size, image_size, 1)

    for ex in data:
        for i in range(28):
            for j in range(28):
                ex[i][j][0] = 0 if ex[i][j][0] == 0 else 1


    import matplotlib.pyplot as plt

    for example, label in zip(data, labels):
        image = np.asarray(example).squeeze()
        plt.imshow(image)
        plt.title("Label: {}".format(label[0]))
        # plt.show()


    container = Container('quadratic',
    DenseBiasLayer(16, activation="sigmoid", eta=0.01), 
    DenseBiasLayer(16, activation="sigmoid", eta=0.01),
    DenseNoBiasLayer(10, activation="sigmoid", eta=0.01))

    xi = data.reshape((-1, 784))

    labels = np.array(labels)
    zeta = []
    for i in range(len(labels)):
        label_array = np.zeros(10)
        label_array[labels[i]] = 1
        zeta.append(label_array)

    zeta = np.array(zeta)

    print(zeta)
    epochs = 50

    for epoch in range(epochs):
        print("epoch", epoch)

        for xi_mu, zeta_mu in zip(xi[:train_size], zeta[:train_size]):
            res, loss = container(xi_mu, zeta_mu, True)

    for xi_mu, zeta_mu in zip(xi[train_size:], zeta[train_size:]):
        res = container.consume(xi_mu)
        print("Expected: {} --- Got: {}".format(np.argmax(zeta_mu), np.argmax(res)))

    return container

# get_mnist_container()

# i = 0
# a = []
# for xi_mu, zeta_mu in zip(xi[180:], zeta[180:]):
#     res, loss = container(xi_mu, zeta_mu, False)
#     a.append(np.argmax(zeta_mu))
#     print("Expected: ", np.argmax(zeta_mu), "/// Got: ", np.argmax(res))

# for example, label in zip(data[180:], labels[180:]):
#     image = np.asarray(example).squeeze()
#     plt.imshow(image)
#     plt.title("Actual: {} ---- Predicted: {}".format(label[0], a[i]))
#     i += 1
#     plt.show()