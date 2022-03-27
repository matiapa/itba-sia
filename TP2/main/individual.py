from tokenize import Number
from typing import Any, ClassVar, Generic, List

class Individual:

    genes: List[float]

    def __init__(self, genes: List[float]) -> None:
        if genes is None:
            genes = self._initialize_genes()

        if len(genes) != self.genome_size():
            raise RuntimeError("The amount of given genes differs from specified genome size")

        self.genes = genes

    """
    Returns the amount of genes the individals that this kind of individual must have
    """
    @staticmethod
    def genome_size() -> int:
        raise NotImplementedError

    """
    Creates a random gene set, method used for creating an initial population
    """
    def _initialize_genes(self) -> List[float]:
        raise NotImplementedError

class IndividualFactory():

    def instantiate(self, genes: List[float]) -> Individual:
        raise NotImplementedError