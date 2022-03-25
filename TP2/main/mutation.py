from individual import Individual
import numpy as np

class Mutation:

    """
    Alters some genes with a certain probability and within certain range.
    This introduces more genetic variety on the population.
    """
    def apply(self, individual: Individual) -> None:
        raise NotImplementedError()

class SampleMutation(Mutation):

    def apply(self, individual: Individual, p: float, sigma: float) -> Individual:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < p:
                individual.genes[i] += np.random.normal(0, sigma)
        
        return individual

class BagMutation(Mutation):
    
    def apply(self, individual: Individual, p: float) -> Individual:
        for i in range(len(individual.genes)):
            if np.random.uniform(0, 1) < p:
                individual.genes[i] = 1 if individual.genes[i] == 0 else 0
        
        return individual