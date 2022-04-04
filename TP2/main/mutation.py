from main.individual import Individual
import numpy as np

class Mutation:

    def __str__(self):
        raise NotImplementedError()
    """
    Alters some genes with a certain probability and within certain range.
    This introduces more genetic variety on the population.
    """
    def apply(self, individual: Individual) -> None:
        raise NotImplementedError()


class UniformIntegerMutation(Mutation):
    def __str__(self):
        return "UniformIntegerMutation" + ' (p=' + str(self.p) + ',' + 'range=' + str(self._range) + ')'

    p: float
    _range: float

    def __init__(self, p: float, _range: float):
        self.p = p
        self._range = _range
    
    def apply(self, individual: Individual) -> None:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < self.p:
                m = round(np.random.uniform(-self._range, self._range))
                individual.genes[i] += m

class UniformMutation(Mutation):

    
    p: float
    _range: float

    def __str__(self):
        return "UniformMutation" + ' (p=' + str(self.p) + ',' + 'range=' + str(self._range) + ')'

    def __init__(self, p: float, _range: float):
        self.p = p
        self._range = _range
    
    def apply(self, individual: Individual) -> None:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < self.p:
                m = np.random.uniform(-self._range, self._range)
                individual.genes[i] += m
        
class NormalMutation(Mutation):

    p: float
    sigma: float

    def __str__(self):
        return "NormalMutation" + ' (p=' + str(self.p) + ',' + 'sigma=' + str(self.sigma) + ')'
    
    def __init__(self, p: float, sigma: float):
        self.p = p
        self.sigma = sigma

    def apply(self, individual: Individual) -> None:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < self.p:
                individual.genes[i] += np.random.normal(0, self.sigma)

class BinaryMutation(Mutation):

    p: float

    def __str__(self):
        return "BinaryMutation" + ' (p=' + str(self.p) + ')'

    def __init__(self, p: float):
        self.p = p
    
    def apply(self, individual: Individual) -> None:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < self.p:
                individual.genes[i] = 1 if individual.genes[i] == 0 else 0