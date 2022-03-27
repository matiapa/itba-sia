from random import random
from typing import List
from main.individual import Individual, IndividualFactory

class PointIndividual(Individual):

    GRID_SIZE = 100

    @staticmethod
    def genome_size() -> int:
        return 2

    def _initialize_genes(self) -> List[float]:
        return [round(random()*PointIndividual.GRID_SIZE), round(random()*PointIndividual.GRID_SIZE)]

    def __str__(self) -> str:
        return str(self.genes)

class PointIndividualFactory(IndividualFactory):

    def instantiate(self, genes: List[float]) -> Individual:
        return PointIndividual(genes)