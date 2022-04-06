from random import random
from typing import List
from main.individual import Individual, IndividualFactory

class BagIndividual(Individual):

    bag_genome_size: int

    @staticmethod
    def genome_size() -> int:
        return BagIndividual.bag_genome_size

    def _initialize_genes(self) -> List[float]:
        return [1 if random() > 0.5 else 0 for i in range(0, BagIndividual.bag_genome_size)]

    def __str__(self) -> str:
        return str(sum(self.genes))

class BagIndividualFactory(IndividualFactory):

    def instantiate(self, genes: List[float]) -> Individual:
        return BagIndividual(genes)