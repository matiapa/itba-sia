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
        # print("DELTA_0", delta) # ok 
        for layer in self.layers[::-1]: 
            delta = layer.update(delta)

container = Container(
    "quadratic", 
    DenseNoBiasLayer(2, activation="id"), 
    DenseNoBiasLayer(2, activation="id"), 
    DenseNoBiasLayer(1, activation="sigmoid"), 
)

# t = [ [1, 1], [1, -1], [-1, -1], [-1, 1]]
# expected = [ [1], [0], [0], [1] ]

# t = [ [1, 1], [1, 2], [3, 4], [-1, -1], [-3, -2]]
# expected = [ [1], [1], [1], [-1], [-1]]

t = []
expected = [] 
for k in range(1000): 
    p = np.random.uniform(-1, 1, (2))
    t.append(p)
    expected.append([1 if p[0]*p[0]+p[1]*p[1] < 1 else 0]) 
    # expected.append([1 if p[1] > 3*p[0]+1 else 0])
    # print(p, 1 if p[0]*p[0]+p[1]*p[1] < 1 else 0)


total_loss = 0 
for epoch in range(10):
    print(epoch)
    for (s, ex) in zip(t, expected): 
        res, loss = container(s, ex, True)
        print(s, res, ex)
        total_loss += loss

# # print(res, "--", total_loss/100, "%")

for i in range(-100, 100): 
    for j in range(-100, 100):
        res = container.consume([i, j]) 
        plt.plot(i/100, j/100, 'k.' if res > 0.5 else 'r.')
plt.show()







