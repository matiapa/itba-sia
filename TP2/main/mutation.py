from individual import Individual

class Mutation:

    """
    Alters some genes with a certain probability and within certain range.
    This introduces more genetic variety on the population.
    """
    def apply(self, individual: Individual) -> None:
        raise NotImplementedError()