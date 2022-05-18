import sys
sys.path.append(".")
sys.path.append("..")

from grapher import graph_confusion_matrix
from container import *
import matplotlib.pyplot as plt
import numpy as np
import gzip


def get_mnist_container(container: Container, items_size, train_size):
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

    # for example, label in zip(data, labels):
    #     image = np.asarray(example).squeeze()
    #     plt.imshow(image)
    #     plt.title("Label: {}".format(label[0]))
    #     plt.show()

    xi = data.reshape((-1, 784))

    labels = np.array(labels)
    zeta = []
    for i in range(len(labels)):
        label_array = np.zeros(10)
        label_array[labels[i]] = 1
        zeta.append(label_array)

    zeta = np.array(zeta)
    epochs = 20

    losses, train_accuracy, test_accuracy = [], [], []
    for epoch in range(epochs):
        print("Epoch", epoch)

        print('Training...')
        global_loss = 0
        for xi_mu, zeta_mu in zip(xi[:train_size], zeta[:train_size]):
            res, loss = container(xi_mu, zeta_mu, True)
            global_loss += loss
        losses.append(global_loss)

        print('Evaluating training accuracy...')
        true_vals = 0
        for xi_mu, zeta_mu in zip(xi[:train_size], zeta[:train_size]):
            res = container.consume(xi_mu)
            if np.argmax(zeta_mu) == np.argmax(res):
                true_vals += 1
            # print("Expected: {} --- Got: {}".format(np.argmax(zeta_mu), np.argmax(res)))
        train_accuracy.append(true_vals / len(xi[:train_size]))

        print('Evaluating test accuracy...')
        true_vals = 0
        for xi_mu, zeta_mu in zip(xi[train_size:], zeta[train_size:]):
            res = container.consume(xi_mu)
            if np.argmax(zeta_mu) == np.argmax(res):
                true_vals += 1
            # print("Expected: {} --- Got: {}".format(np.argmax(zeta_mu), np.argmax(res)))
        test_accuracy.append(true_vals / len(xi[train_size:]))

    plt.plot([i for i in range(epochs)], losses)
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.yscale('log')
    plt.show()

    # plt.plot([i for i  in range(epochs)], train_accuracy, label='Train')
    # plt.plot([i for i  in range(epochs)], test_accuracy, label='Test')
    # plt.xlabel('Epoch')
    # plt.ylabel('Accuracy')
    # plt.yscale('log')
    # plt.legend()
    # plt.show()

    return container, xi, zeta

# ----------------- ANALISIS -------------------------------

def confusion_matrix(xi, zeta, container):
    matrix = np.zeros((10, 10)).tolist()

    i=0
    for xi_mu, zeta_mu in zip(xi, zeta):
        if i % 10 == 0:
            print(f'{i}/{len(xi)}')
        psi_mu = container.consume(xi_mu)
        
        expected_num = np.argmax(zeta_mu)
        output_num = np.argmax(psi_mu)
        
        matrix[expected_num][output_num] += 1

        # print(f'Expected: {expected_num}')
        # print(f'Output: {output_num}')
        # print('--------------')
        i += 1
    
    return matrix


container = Container('quadratic',
    DenseBiasLayer(16, activation="sigmoid", eta=0.01), 
    DenseBiasLayer(16, activation="sigmoid", eta=0.01),
    DenseNoBiasLayer(10, activation="sigmoid", eta=0.01)
)

i = 0
for x in container.layers: 
    print("Deserializing layer {}".format(i))
    x.w = np.load("layer{}.npy".format(i))
    # print(x.w)
    x.born = True
    i += 1

container, xi, zeta = get_mnist_container(
    container, 
    items_size=10000, 
    train_size=9900
)

matrix = confusion_matrix(xi[9900:], zeta[9900:], container)

# graph_confusion_matrix('Digit recognition confusion matrix', [f'{n}' for n in range(10)], matrix)

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