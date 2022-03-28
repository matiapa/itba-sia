import sys
sys.path.append("..")
sys.path.append("../..")

from fitness import ReactiveFitness, F, inputs
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
    print("\n", end="\n")
    print(f"Generation {t}", end="\n")
    for i in individuals:
        print(i, end='\n')
        print("Fitness aka AntiError: ", ReactiveFitness().apply(i), end="\n")
        print("Funcion F: ", F(i.W, i.w, i.w_0, inputs["xi"][0]), end="\n")

    t += 1