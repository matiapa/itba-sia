import sys
sys.path.append("..")
sys.path.append("../..")

from fitness import ReactiveFitness
from individual import ReactiveIndividual, ReactiveIndividualFactory

from typing import List

from main.algorithm import Algorithm
from main.crossing.uniform_cross import SimpleCross
from main.mutation import UniformIntegerMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.elite_selection import EliteSelection
from main.selection.roulette_selection import RouletteSelection

from main.algorithm import Algorithm

fitness = ReactiveFitness()

algorithm = Algorithm(
    ind_factory = ReactiveIndividualFactory(), pairing = ElitistPairing(), cross = SimpleCross(p=0),
    mutation = UniformIntegerMutation(p=1, _range=5), fitness = fitness, selection = EliteSelection(),
    init_pop_size = 10
)
iterator = iter(algorithm)

t = 0
while t < 10:
    individuals : List[ReactiveIndividual] = next(iterator)

    for i in individuals:
        print(i, end='\n')

    t += 1