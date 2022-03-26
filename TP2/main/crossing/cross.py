from main.individual import Individual, IndividualFactory
from typing import List, Tuple
class Cross:

    """
    Produces exactly two individuals by mixing the genes of another
    set of exactly two individuals (their parents)
    """
    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory) -> Tuple[Individual, Individual]:
        raise NotImplementedError()