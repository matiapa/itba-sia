from operator import itemgetter
import numpy as np


class Oja:

    def __init__(self, eta: float, iterations: int):
        self.eta = eta
        self.iterations = iterations

    def train(self, w0: list[float], inputs: list[list[float]]) -> np.ndarray:
        self.weights_t = []
        weights = np.array(w0)

        for i in range(self.iterations):
            self.weights_t.append(np.array(weights))

            for input in inputs:
                s = np.inner(np.array(input), weights)
                weights += self.eta * s * (np.array(input) - s * weights)

            print(weights)
            print('----------------------')
        
        return self.weights_t