from random import random
import sys
sys.path.append("..")

from container import * 
from grapher import * 
import numpy
import sklearn


def train(psi, zeta):
    epochs = 100

    container = Container(
        "quadratic", 
        DenseBiasLayer(16, activation="sigmoid", eta=0.01),
        DenseBiasLayer(16, activation="sigmoid", eta=0.01),
        DenseNoBiasLayer(10, activation="id", eta=0.01)
    )

    errors, train_accuracy, test_accuracy = [], [], []
    i = 0

    for epoch in range(epochs): 
        print(f'---------------- Epoch {epoch} ----------------')

        # Feed psis in random order
        psi, zeta = sklearn.utils.shuffle(psi, zeta)

        error = 0
        psi_num = 0
        for psi_mu, zeta_mu in zip(psi, zeta):
            res, loss = container(psi_mu, zeta_mu, True)
            error += loss
            print(f'Num: {psi_num}')
            print(f'Out: {[round(x) for x in res]}')
            print(f'Expected: {[round(x) for x in zeta_mu]}')
            print('--------------')
            psi_num += 1
        errors.append(error)

        print('Evaluating training accuracy...')

        true_vals = 0
        for xi_mu, zeta_mu in zip(psi, zeta):
            res = container.consume(xi_mu)
            if np.argmax(zeta_mu) == np.argmax(res):
                true_vals += 1
        train_accuracy.append(true_vals / len(psi))

        print('Evaluating test accuracy...')

        # noised_input = list(psi)
        # for input in noised_input:
        #     for num in range(len(input)):
        #         if random() < 0.02:
        #             input[num] = 0 if input[num]==1 else 0

        # true_vals = 0
        # for xi_mu, zeta_mu in zip(noised_input, zeta):
        #     res = container.consume(xi_mu)
        #     if np.argmax(zeta_mu) == np.argmax(res):
        #         true_vals += 1
        # test_accuracy.append(true_vals / len(noised_input))

    plt.plot(range(len(errors)), errors, 'k-')
    # plt.yscale("log")
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.show()

    plt.plot([i for i  in range(epochs)], train_accuracy, label='Train')
    # plt.plot([i for i  in range(epochs)], test_accuracy, label='Test')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    # plt.yscale('log')
    plt.legend()
    plt.show()
       
    return container

def confusion_matrix():
    matrix = np.zeros((10, 10)).tolist()

    for s in range(10):
        # Add some noise to inputs

        noised_input = psi.copy()
        for input in noised_input:
            for num in range(len(input)):
                if random() < 0.02:
                    input[num] = 0 if input[num]==1 else 0

        print("Evaluating with noise")

        # Evaluate them

        for num in range(len(noised_input)):
            input = noised_input[num]
            output = container.consume(input)
            
            input_num = num
            output_num = numpy.argmax(output)
            
            matrix[input_num][output_num] += 1

            print(f'Input: {input_num}')
            print(f'Output: {output_num}')
            print('--------------')
    
    graph_confusion_matrix('Digit recognition confusion matrix', [f'{n}' for n in range(10)], matrix)

if __name__ == "__main__":
    # Read training data from file

    psi = [[],[],[],[],[],[],[],[],[],[]]   # 10 x 35
    zeta = numpy.identity(10).tolist()

    with open("../inputs/digits_map_train_set.txt", "r") as f:
        line_num = 0 
        for line in f.readlines():
            psi_num = line_num // 7
            for pixel in line.split(" "):
                psi[psi_num].append(int(pixel))
            line_num +=1

    # Train the network

    container = train(psi, zeta)

    # confusion_matrix()