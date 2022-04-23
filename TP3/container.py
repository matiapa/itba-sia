from cmath import exp
from math import e
from turtle import ycor
from layer import * 
import numpy as np 


class Perceptron: 
    


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
    DenseBiasLayer(4, activation="id"), 
    DenseBiasLayer(2, activation="id"), 
    DenseNoBiasLayer(2, activation="id"), 
)


