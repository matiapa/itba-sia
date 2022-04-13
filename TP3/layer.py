from typing import List
import numpy as np 
from matplotlib import pyplot as plt 

class Layer: 

    def __init__(self):
        self.born = False

    def build(self, input_shape: int):
        pass
    
    def call(self, input: np.ndarray):
        pass 

    def __call__(self, input: np.ndarray): 
        if not self.born: 
            self.born = True 
            self.build(len(input))
        return self.call(input) 
    
    def update_weights(self, delta): 
        pass 
    
    def new_delta(self, delta): 
        pass 

    def update(self, delta): 
        self.update_weights(delta)
        return self.new_delta(delta)
    
class DenseNoBiasLayer(Layer): 

    activations = {
        "relu": [lambda x: np.maximum(0, x), lambda x: 1 if x > 0 else 0], 
        "sigmoid": [lambda x: 1 / (1+np.exp(-x)), lambda x: (1 / (1+np.exp(-x)))*(1-(1 / (1+np.exp(-x))))],
        "id": [lambda x: x, lambda x: 1], 
        "step": [lambda x: np.sign(x), lambda x: 0], 
        "caca": [lambda x: 2*x, lambda x: 3*x]
    }

    def __init__(self, units: int, activation: str):
        super().__init__()
        self.units = units
        self.g = DenseNoBiasLayer.activations[activation]

        # caches 
        self.last_input = None 
        self.last_z = None 
        self.diagonal_matrix = None 

    def build(self, input_shape: int):
        self.w = np.random.normal( 0, 1, (self.units, input_shape) ) # Perhaps N~(0, 1) is better
    
    def call(self, input: np.ndarray):
        self.last_z = np.matmul(self.w, input)
        self.last_input = np.array([input])
        nonlinear =  self.g[0](self.last_z)
        # print("Input", input)
        # print("W", self.w)
        # print("Z", self.last_z)
        # print("NONLINEAR", nonlinear)
        return nonlinear 

    
    def update_weights(self, delta: np.ndarray): 
        self.diagonal_matrix = np.zeros((self.units, self.units))
        # print("EMPTY DIAGONAL", self.diagonal_matrix)
        for i in range(self.units): 
            self.diagonal_matrix[i][i] =  (self.g)[1](self.last_z[i])
        # print("FULL DIAGONAL", self.diagonal_matrix)
        # print("DELTA", delta)
        # print("LAST INPUT", self.last_input)
        # print("OLD_W", self.w)
        self.w = self.w - 0.1*np.array(np.matmul(np.matmul(self.diagonal_matrix, delta), self.last_input))
        # print("NEW_W", self.w)
    
    def new_delta(self, delta: np.ndarray): 
        return np.matmul(np.matmul(np.transpose(self.w), self.diagonal_matrix), delta) 





