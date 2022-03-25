from typing import List, Tuple
from individual import Individual, IndividualFactory

class Cross:

    """
    Produces exactly two individuals by mixing the genes of another
    set of exactly two individuals (their parents)
    """
    def apply(self, i1: Individual, i2: Individual, factory: IndividualFactory) -> Tuple[Individual, Individual]:
        raise NotImplementedError()