from main.individual import Individual, IndividualFactory
from main.crossing.cross import Cross

from typing import List, Tuple
import numpy as np

"""
Chooses 'npoints' random cutting points and mixes parent genomes using those points
For example:
    With npoints = 2,   i1 = A B A B A B    you get     n1 = A B B A A B
                        i2 = B A B A B A                n2 = B A A B B A
    Supposing that the chosen cutting points were = [0, 2, 4, 6]
"""
class MultipleCross(Cross):

    npoints: int
    points: List[int] = []

    def __str__(self):
        return "MultipleCross" + ' (npoints = ' + str(self.npoints) + ')'

    def __init__(self, npoints: int, points: List[int] = []):
        self.npoints = npoints
        self.points = points

    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory) -> Tuple[Individual, Individual]:

        # You should not cross a worm with a human!
        if type(i1) != type(i2):
            raise RuntimeError("Individuals must be of the same type")

        # Note that individuals of same type have the same genome size
        genome_size = i1.genome_size()

        # If no cutting points were given, generate a list of random ones
        if len(self.points) == 0:
            self.points = list(np.random.choice(range(1, genome_size-1), size=self.npoints, replace=False))

        self.points.append(0)
        self.points.append(genome_size)
        self.points.sort()

        # Fill up the genomes of the new individuals

        n1_genes = []
        n2_genes = []

        for i in range(0, len(self.points)-1):
            p1 = self.points[i]
            p2 = self.points[i+1]

            n1_src = i1 if i % 2 else i2
            n2_src = i2 if i % 2 else i1

            n1_genes += n1_src.genes[p1:p2]
            n2_genes += n2_src.genes[p1:p2]

        # Instantiate the new individuals and return them

        return factory.instantiate(n1_genes), factory.instantiate(n2_genes)