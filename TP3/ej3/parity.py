from random import random
import sys
sys.path.append("..")

from container import * 
from grapher import * 
import numpy
import sklearn


def train(psi, zeta, plot_error):
    epochs = 50

    container = Container(
        "quadratic", 
        DenseBiasLayer(50, activation="sigmoid", eta=0.01),
        DenseBiasLayer(10, activation="relu", eta=0.01),
        DenseBiasLayer(1, activation="id", eta=0.01),
    )

    errors = [] 
    i = 0

    for epoch in range(epochs): 
        print(f'---------------- Epoch {epoch} ----------------')

        # Feed psis in random order
        array1_shuffled, array2_shuffled = sklearn.utils.shuffle(psi, zeta)

        error = 0
        psi_num = 0
        for psi_mu, zeta_mu in zip(psi, zeta):
            res, loss = container(psi_mu, zeta_mu, True)
            error += loss
            
            print(f'Num: {psi_num}')
            print(f'Out: {[x for x in res]}')
            print(f'Expected: {zeta_mu}')
            print('--------------')
            psi_num += 1

        i += 1

        errors.append(error)
        if error < 1e-9: 
            break

    if plot_error:
        plt.plot(range(len(errors)), errors, 'k-')
        plt.yscale("log")
        plt.xlabel('Epoch')
        plt.ylabel('Error')
        plt.show()

    return container

def confusion_matrix():
    matrix = np.zeros((2, 2)).tolist()

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
            
            input_parity = 1 if num % 2 == 0 else 0
            output_parity = min(1, round(output[0]))
            
            print(f'Input num: {num}')
            print(f'Input parity: {input_parity}')
            print(f'Output parity: {output_parity}')
            print('--------------')

            matrix[input_parity][output_parity] += 1
    
    graph_confusion_matrix('Digit parity confusion matrix', ['Even', 'Odd'], matrix)

if __name__ == "__main__":
    # Read training data from file

    psi = [[],[],[],[],[],[],[],[],[],[]]   # 10 x 35
    zeta = [[1],[0],[1],[0],[1],[0],[1],[0],[1],[0]]

    with open("../inputs/digits_map_train_set.txt", "r") as f:
        line_num = 0 
        for line in f.readlines():
            psi_num = line_num // 7
            for pixel in line.split(" "):
                psi[psi_num].append(int(pixel))
            line_num +=1

    container = train(psi, zeta, True)

    confusion_matrix()