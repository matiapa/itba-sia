from random import random
from typing import List

import numpy
from main.individual import Individual, IndividualFactory

class PointIndividual(Individual):

    GRID_SIZE = 100

    @staticmethod
    def genome_size() -> int:
        return 2

    def _initialize_genes(self) -> List[float]:
        x,y = numpy.random.uniform(0, PointIndividual.GRID_SIZE-1, size=2)
        return [round(x), round(y)]

    def __str__(self) -> str:
        return str(self.genes)

class PointIndividualFactory(IndividualFactory):

    def instantiate(self, genes: List[float]) -> Individual:
        return PointIndividual(genes)