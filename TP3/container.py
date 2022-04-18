from cmath import exp
from math import e
from turtle import ycor
from layer import * 
import numpy as np 

class Container: 

    losses = {
        "quadratic": [ lambda y, a: sum(np.square(np.subtract(y, a))), lambda y, a: [[-2*(y_i-a_i)] for (y_i, a_i) in zip(y, a)]], # TODO: check 
    }

    def __init__(self, loss_fun: str, *args: Layer): 
        self.loss = Container.losses[loss_fun] 
        self.layers = args
        
    def __call__(self, input: np.ndarray, expected_output: np.ndarray, train: bool):
        input = np.array(input)
        expected_output = np.array(expected_output)
        res = self.consume(input)
        if len(res) != len(expected_output): 
            raise Exception('Something went wrong: len(expected_output) != len(res)')
        if train:
            self.backpropagation(res, expected_output) 
        return res, self.loss[0](expected_output, res)

    def consume(self, input: np.ndarray):
        res = input
        for layer in self.layers: 
            res = layer(res)
        return res

    def backpropagation(self, actual_output: np.ndarray, expected_output: np.ndarray): 
        delta = np.array(self.loss[1](expected_output, actual_output))
        print("DELTA_0", delta) # ok 
        for layer in self.layers[::-1]: 
            delta = layer.update(delta)


# TODO: Sin Bias, no debería siquiera funcionar 
container = Container(
    "quadratic", 
    DenseBiasLayer(100, activation="sigmoid"), 
    DenseNoBiasLayer(1, activation="sigmoid"), 
)


# t = np.random.uniform(-1, 1, (20, 2))
# expected = [ 1.0 if p[0] > 0 and p[1] > 0 else 0.0 for p in t]
t = [ [1,1], [-1, 1], [1, -1], [-1, -1]]
expected = [ 0, 1, 1, 0]

i = 0 
for epoch in range(100): 
    for x, label in zip(t, expected): 
        plt.plot(x[0], x[1], 'k+' if label == 1 else 'rx')
        res, loss = container(x, [label], train=True)
        print(res)

flag = 1
for i in range(-10, 10):
    for j in range(-10, 10): 
        res = container.consume([i/10, j/10])
        print("res[0]", res[0])
        if  not np.isnan(res[0]) and res[0] >= 0.5:
            plt.plot(i/10, j/10, 'go')
        # elif not np.isnan(res[0]) and res[0] < 0.5:
        #     plt.plot(i/100, j/100, 'b.')
        else: 
            flag = 0 

# print("OF THE LEFT ZERO", container.consume([-0.10, -0.10]))

# print("OF THE ZERO", container.consume([0, 0]))
# print("OF THE RIGHT ZERO", container.consume([0.10, 0.10]))


plt.show()

# container([2, 3], [1], train=True)









