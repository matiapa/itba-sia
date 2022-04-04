from multiprocessing import freeze_support
import sys
sys.path.append("..")
sys.path.append("../..")

from main.selection.truncated_selection import TruncatedSelection
from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.rank_selection import RankSelection
from main.selection.elite_selection import EliteSelection
from main.pairing.elitist_pairing import ElitistPairing
from main.mutation import UniformIntegerMutation, UniformMutation
from main.crossing.simple_cross import SimpleCross
from main.algorithm import Algorithm
from typing import List
from individual import ReactiveIndividual, ReactiveIndividualFactory
from fitness import ReactiveFitness, F, inputs

fitness = ReactiveFitness()

algorithm = Algorithm(
    ind_factory=ReactiveIndividualFactory(), 
    pairing=ElitistPairing(), 
    cross=SimpleCross(),
    mutation=UniformMutation(p=0.5, _range=0.1), 
    fitness=fitness, 
    selection=RankSelection(),
    init_pop_size=100
)
iterator = iter(algorithm)


t = 0
while t < 500:
    individuals: List[ReactiveIndividual] = next(iterator)
    print("\n", end="\n")
    print(f"Generation {t}", end="\n")
    for i in individuals:
        print(i, end='\n')
        print("Fitness aka AntiError: ", ReactiveFitness().apply(i), end="\n")
        print("Funcion F: 0 ", F(i.W, i.w, i.w_0, inputs["xi"][0]), end="\n")
        print("Funcion F: 1 ", F(i.W, i.w, i.w_0, inputs["xi"][1]), end="\n")
        print("Funcion F: 2 ", F(i.W, i.w, i.w_0, inputs["xi"][2]), end="\n")
    t += 1


# algorithmParallel = AlgorithmParallel(
#     ind_factory = ReactiveIndividualFactory(), pairing = ElitistPairing(), cross = UniformCross(p=0),
#     mutation = UniformIntegerMutation(p=1, _range=5), fitness = fitness, selection = RankSelection(),
#     init_pop_size = 100,
#     join_gens=100
# )

# freeze_support()

# algorithmParallel.run_multiple()