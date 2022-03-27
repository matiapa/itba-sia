from main.individual import Individual, IndividualFactory
from main.crossing.cross import Cross

from typing import Tuple
import numpy as np

"""
Each gene is mixed with its counterpart with a probability 'p'
"""
class SimpleCross(Cross):

    p: float

    def __init__(self, p: float) -> None:
        self.p = p

    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory) -> Tuple[Individual, Individual]:

        # You should not cross a worm with a human!
        if type(i1) != type(i2):
            raise RuntimeError("Individuals must be of the same type")

        # Note that individuals of same type have the same genome size
        genome_size = i1.genome_size()

        n1_genes = i1.genes.copy()
        n2_genes = i2.genes.copy()

        for i in range(0, genome_size):
            n = np.random.uniform(0, 1)
            if n < self.p:
                n1_genes[i] = i2.genes[i]
                n2_genes[i] = i1.genes[i]

        return factory.instantiate(n1_genes), factory.instantiate(n2_genes)