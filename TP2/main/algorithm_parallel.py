import multiprocessing
from main.algorithm import Algorithm
from main.crossing.cross import Cross
from main.pairing.pairing import Pairing
from main.selection.selection import Selection
from main.fitness import Fitness
from main.mutation import Mutation
from main.individual import Individual, IndividualFactory

from multiprocessing import Pool, cpu_count
from typing import List

class AlgorithmParallel:

    def __init__(
        self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, \
        fitness: Fitness, selection: Selection, init_pop_size: int, join_gens: int
    ) -> None:
        self.init_pop_size = init_pop_size
        self.pool_size = cpu_count()
        self.algorithms = [
            Algorithm(ind_factory, pairing, cross, mutation, fitness, selection, init_pop_size) \
                for i in range(0, init_pop_size // self.pool_size)
        ]
        self.join_gens = join_gens

    def run_single(self, algorithm: Algorithm) -> List[Individual]:
        it, sub_pop = iter(algorithm), None
        for t in range(self.join_gens):
            sub_pop = next(it)
        return sub_pop

    def run_multiple(self):
        pool = Pool(8)
        results = [pool.apply(self.run_single(self.algorithms[i])) for i in range(self.pool_size)]
        pool.close()

        print(results)