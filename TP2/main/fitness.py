from main.individual import Individual

class Fitness:

    """
    Determines the fitness score of an individual, this is a measure
    of how ideal it is as a solution to the problem we're trying to solve
    """
    def apply(self, individual: Individual) -> float:
        raise NotImplementedError()