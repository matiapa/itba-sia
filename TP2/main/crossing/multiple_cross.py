from typing import List, Tuple, TypeVar
from individual import Individual, IndividualFactory
from cross import Cross
import numpy as np

"""
Chooses 'npoints' random cutting points and mixes parent genomes using those points
For example:
    With  i1 = A B A B A B  and  i2 = B A B A B A  and  npoints = 2
    You may get cutting points = [0, 2, 4, 6]
    Then  n1 = A B B A A B  and  n2 = B A A B B A
"""
class MultipleCross(Cross):

    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory, npoints: int) -> Tuple[Individual, Individual]:

        # You should not cross a worm with a human!
        if type(i1) != type(i2):
            raise RuntimeError("Individuals must be of the same type")

        # Note that individuals of same type have the same genome size
        genome_size = i1.genome_size

        # Generate a list of random cutting points

        points: List[int] = np.random.choice(range(1, genome_size-1), size=npoints, replace=False)
        points.append(0)
        points.append(genome_size)
        points.sort()

        # Fill up the genomes of the new individuals

        n1_genes = []
        n2_genes = []

        for i in range(0, len(points)-1):
            p1 = points[i]
            p2 = points[i+1]

            n1_src = i1 if i % 2 else i2
            n2_src = i2 if i % 2 else i1

            n1_genes += n1_src.genes[p1:p2]
            n2_genes += n2_src.genes[p1:p2]

        # Instantiate the new individuals and return them

        return factory.instantiate(n1_genes), factory.instantiate(n2_genes)