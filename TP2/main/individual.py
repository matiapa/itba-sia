from typing import Any, Generic, List

from fitness import Fitness

class Individual():

    genes: List[float]

    def __init__(self, genes: List[float]) -> None:
        if genes is None:
            genes = self.__initialize_genes()
        self.genes = genes

    """
    Creates a random gene set, method used for creating an initial population
    """
    def __initialize_genes(self):
        raise NotImplementedError


class IndividualFactory():

    def instantiate(self, genes: List[float]) -> Individual:
        raise NotImplementedError