from typing import List, Tuple
from individual import Individual, IndividualFactory
from cross import Cross
import numpy as np

"""
Each gene is mixed with its counterpart with a probability 'p'
"""
class SimpleCross(Cross):

    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory, p: int) -> Tuple[Individual, Individual]:

        # You should not cross a worm with a human!
        if type(i1) != type(i2):
            raise RuntimeError("Individuals must be of the same type")

        # Note that individuals of same type have the same genome size
        genome_size = i1.genome_size  

        n1_genes = i1.genes
        n2_genes = i2.genes

        for i in range(0, genome_size):
            n = np.random.uniform(0, 1)
            if n < p:
                n1_genes[i] = i2.genes[i]
                n2_genes[i] = i1.genes[i]

        return factory.instantiate(ni_genes), factory.instantiate(ni_genes)