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


    def __init__(
        self, ind_factory: IndividualFactory, pairing: Pairing, cross: Cross, mutation: Mutation, \
        fitness: Fitness, selection: Selection, init_pop_size: int
    ) -> None:
        self.ind_factory = ind_factory
        self.pairing = pairing
        self.cross = cross
        self.mutation = mutation
        self.fitness = fitness
        self.selection = selection
        self.init_pop_size = init_pop_size

    
    def __iter__(self):
        # Create an initial population of silly beings

        self.population : List[Individual] = []
        self.generation = 0

        for _ in range(0, self.init_pop_size):
            individual = self.ind_factory.instantiate(genes = None)
            self.population.append(individual)

        return self


    def __next__(self):
        # Make pairs of individuals that will love each other for eternity

        pairs = self.pairing.apply(self.population, self.fitness)
        if len(pairs) != len(self.population) / 2:
            raise RuntimeError("Invalid pairing method, it must return exactly N/2 pairs being N the population size")
        
        # Create new beings from the previous pairs

        # print('PARENTS')
        # for i in self.population:
        #     print(f'{i.genes[0], i.genes[1], self.fitness.apply(i)}', end=' ')
        # print('')

        # s = time.time_ns()
        new_population = []
        for pair in pairs:
            n1, n2 = self.reproduce(pair)
            new_population.append(n1)
            new_population.append(n2)
        self.population += new_population
        # print(f'Reproduction: {(time.time_ns() - s) / 1e6} ms')

        # print('CHILDRENS')
        # for i in new_population:
        #     print(f'{i.genes[0], i.genes[1], self.fitness.apply(i)}', end=' ')
        # print('')

        # Select the glorious beings that will thrive and survive

        # for i in self.population:
        #     print(f'{i.genes[0], i.genes[1], round(self.fitness.apply(i), 6)}', end=' ')
        # print('')

        self.population = self.selection.apply(individuals = self.population, fitness = self.fitness)

        self.generation += 1

        return self.population


    def reproduce(self, pair: Tuple[Individual, Individual]):
        

        # Give the individuals the miracle of creating new beings
        i1, i2 = self.cross.apply(i1 = pair[0], i2 = pair[1], factory = self.ind_factory)

        # Mutate the new ones and hope they wont become parasites
        self.mutation.apply(i1)
        self.mutation.apply(i2)

        # Incorporate them to our new population
        return [i1, i2]