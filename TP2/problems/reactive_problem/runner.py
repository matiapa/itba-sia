import sys
sys.path.append("..")
sys.path.append("../..")

from fitness import ReactiveFitness, F, inputs
from individual import ReactiveIndividual, ReactiveIndividualFactory

from typing import List

from main.algorithm import Algorithm
from main.crossing.uniform_cross import UniformCross
from main.mutation import UniformIntegerMutation
from main.pairing.elitist_pairing import ElitistPairing
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection


from main.algorithm import Algorithm

fitness = ReactiveFitness()

algorithm = Algorithm(
    ind_factory = ReactiveIndividualFactory(), pairing = ElitistPairing(), cross = UniformCross(p=0),
    mutation = UniformIntegerMutation(p=1, _range=5), fitness = fitness, selection = RankSelection(),
    init_pop_size = 100
)
iterator = iter(algorithm)

t = 0
while t < 100:
    individuals : List[ReactiveIndividual] = next(iterator)
    print("\n", end="\n")
    print(f"Generation {t}", end="\n")
    for i in individuals:
        print(i, end='\n')
        print("Fitness aka AntiError: ", ReactiveFitness().apply(i), end="\n")
        print("Funcion F: ", F(i.W, i.w, i.w_0, inputs["xi"][1]), end="\n")

    t += 1