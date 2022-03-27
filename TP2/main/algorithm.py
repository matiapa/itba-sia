from time import time
from turtle import back
from main.crossing.cross import Cross
from main.pairing.pairing import Pairing
from main.selection.selection import Selection
from main.fitness import Fitness
from main.mutation import Mutation
from main.stop_criteria import StopCriteria
from individual import Individual, IndividualFactory

import time
import numpy
import multiprocessing
from joblib import Parallel, delayed
from typing import List, Tuple

class Algorithm:

    ind_factory: IndividualFactory
    pairing: Pairing
    cross: Cross
    mutation: Mutation
    fitness: Fitness
    selection: Selection
    stop_criteria: StopCriteria
    

    def __init__(self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, fitness: Fitness, \
            selection: Selection, stop_criteria: StopCriteria, init_pop_size: int) -> None:
        self.ind_factory = ind_factory
        self.pairing = pairing
        self.cross = cross
        self.mutation = mutation
        self.fitness = fitness
        self.selection = selection
        self.init_pop_size = init_pop_size
        self.stop_criteria = stop_criteria

    def reproduce(self, pair: Tuple[Individual, Individual]):
        # Give the individuals the miracle of creating new beings
        i1, i2 = self.cross.apply(i1 = pair[0], i2 = pair[1], factory = self.ind_factory)

        # Mutate the new ones and hope they wont become parasites
        self.mutation.apply(i1)
        self.mutation.apply(i2)

        # Incorporate them to our new population
        return [i1, i2]
    
    def run(self) -> List[Individual]:
        # Create an initial population of silly beings

        self.population : List[Individual] = []
        
        for _ in range(0, self.init_pop_size):
            individual = self.ind_factory.instantiate(genes = None)
            self.population.append(individual)

        # Evolve until Singularity happens or the universe reaches thermal death

        generation = 0
        while not self.stop_criteria.should_stop(population = self.population, fitness = self.fitness, generation = generation):
            new_population : List[Individual] = []

            # Make pairs of individuals that will love each other for eternity

            # s = time.time_ns()
            pairs = self.pairing.apply(self.population, self.fitness)
            if len(pairs) != len(self.population) / 2:
                raise RuntimeError("Invalid pairing method, it must return exactly N/2 pairs being N the population size")
            # print(f'Pairing: {(time.time_ns() - s)/1e6} ms')

            # Create the new beings

            # s = time.time_ns()
            for pair in pairs:
                n1, n2 = self.reproduce(pair)
                new_population.append(n1)
                new_population.append(n2)
            # results = Parallel(n_jobs=8)(delayed(self.reproduce)(pair) for pair in pairs)
            # new_population = numpy.array(results).flatten().tolist()
            # print(f'Reproduction: {(time.time_ns() - s)/1e6} ms')

            # Select the glorious beings that will thrive and survive

            # s = time.time_ns()
            self.population = self.selection.apply(individuals = self.population + new_population, fitness = self.fitness)
            # print(f'Selection: {(time.time_ns() - s)/1e6} ms')
            # print('-------------------------')

            generation += 1

        return self.population