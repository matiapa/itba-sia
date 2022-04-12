from typing import List
import numpy as np 
from matplotlib import pyplot as plt 

class Layer: 

    def __init__(self):
        self.born = False 

    def build(self, input_shape: int):
        raise '\'build()\' on Layer not implemented' 

    def call(self, input: np.ndarray): 
        raise '\'call()\' on Layer not implemented'

    def __call__(self, input: np.ndarray): 
        if not self.born: 
            self.born = True 
            self.build(len(input))
        return self.call(input) 


class DenseNoBiasLayer(Layer): 

    activations = {
        "relu": lambda x: np.max(0, x), 
        "sigmoid": lambda x: 1 / (1+np.exp(-x)),
        "tanh": lambda x: np.tanh(x), 
        "id": lambda x: x, 
        "step": lambda x: np.sign(x)
    }

    def __init__(self, units: int, activation: str):
        super().__init__()
        self.units = units
        self.g = DenseNoBiasLayer.activations[activation]

    def build(self, input_shape: int):
        self.w = np.random.rand(self.units, input_shape)
    
    def call(self, input: np.ndarray):
        print("MULTIPLYING")
        return self.g(np.matmul(self.w, np.array(input)))





