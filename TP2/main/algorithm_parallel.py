from main.algorithm import Algorithm
from main.crossing.cross import Cross
from main.pairing.pairing import Pairing
from main.selection.selection import Selection
from main.fitness import Fitness
from main.mutation import Mutation
from main.individual import Individual, IndividualFactory

from multiprocessing import Pool, cpu_count
from typing import List, Set
import numpy as np

class AlgorithmParallel:

    def __init__(
        self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, \
        fitness: Fitness, selection: Selection, init_pop_size: int, generations: int
    ) -> None:
        self.init_pop_size = init_pop_size
        self.pool_size = cpu_count()
        self.algorithms = [
            Algorithm(ind_factory, pairing, cross, mutation, fitness, selection, init_pop_size // self.pool_size) \
            for i in range(0, init_pop_size // self.pool_size)
        ]
        self.generations = generations

    def run_single(self, algorithm: Algorithm) -> List[Individual]:
        it = iter(algorithm)
        for t in range(self.generations):
            sub_pop = next(it)
        return list(sub_pop)

    def run_multiple(self) -> List[Individual]:
        pool = Pool(self.pool_size)
        populations = pool.map(self.run_single, self.algorithms)
        pool.close()
        return np.array(populations).flatten()