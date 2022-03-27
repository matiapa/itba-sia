from random import random
from typing import List
from main.individual import Individual, IndividualFactory

class BagIndividual(Individual):

    @staticmethod
    def genome_size() -> int:
        return 100

    def _initialize_genes(self) -> List[float]:
        return [1 if random() > 0.5 else 0 for i in range(0,100)]

class BagIndividualFactory(IndividualFactory):

    def instantiate(self, genes: List[float]) -> Individual:
        return BagIndividual(genes)