import sys
sys.path.append("..")
sys.path.append("../..")
sys.path.append("../../..")

from main.selection.boltzmann_selection import BoltzmannSelection
from main.selection.elite_selection import EliteSelection
from main.selection.rank_selection import RankSelection
from main.selection.roulette_selection import RouletteSelection
from main.selection.softmax_selection import SoftmaxSelection
from main.selection.tournament_selection import TournamentSelection
from main.selection.truncated_selection import TruncatedSelection
from main.mutation import NormalMutation
from main.mutation import UniformMutation
from main.crossing.uniform_cross import UniformCross
from main.crossing.multiple_cross import MultipleCross
from main.pairing.elitist_pairing import ElitistPairing
from main.algorithm import Algorithm

from problems.reactive_problem.individual import ReactiveIndividualFactory
from problems.reactive_problem.fitness import ReactiveFitness

import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Pool, cpu_count


t0 = 10
TC = np.arange(0.1, 1, 0.1)           # Range for final temperature
K = np.arange(0.01, 0.1, 0.01)        # Range for decayment ration
U = np.arange(0.50, 1, 0.05)          # Range for probability in tournament selection

ITERATIONS = 500
POP_SIZE = 50

fitness = ReactiveFitness()

def run(cross, selection, mutation):
    algorithm = Algorithm(
        ind_factory = ReactiveIndividualFactory(), 
        pairing = ElitistPairing(), 
        cross = cross,
        mutation = mutation,
        fitness = fitness,
        selection = selection,
        init_pop_size = POP_SIZE
    )
    iterator = iter(algorithm)

    fitnesses = []

    for _ in range(ITERATIONS):
        population = next(iterator)
        fitnesses += [fitness.apply(_) for _ in population]

    return fitnesses

short_labels = {
    UniformCross: "UC", MultipleCross: "MC", BoltzmannSelection: "BS", EliteSelection: "ES", RankSelection: "RaS", RouletteSelection: "RoS",
    SoftmaxSelection: "SS", TournamentSelection: "ToS", TruncatedSelection: "TrS", UniformMutation: "UM", NormalMutation: "NM"
}

def worker(args):
    fitnesses = run(cross=UniformCross(p=0.9), selection=args[0], mutation=args[1])
    max = np.max(fitnesses)
    min = np.min(fitnesses)
    avg = np.average(fitnesses)
    std = np.std(fitnesses)
    label = f"{short_labels[type(args[0])]}, {short_labels[type(args[1])]}"
    print(label)
    return (max, min, avg, std, label)

def cartesian(A, B):
    return [(a,b) for a in A for b in B]

def permutation_compare():
    selections = [BoltzmannSelection(tc=10, to=1, k=0.1), EliteSelection(), RankSelection(), \
        RouletteSelection(), SoftmaxSelection(), TournamentSelection(u=0.9), TruncatedSelection(k=7)]

    mutations = [UniformMutation(p=0.9, _range=0.1), NormalMutation(p=0.9, sigma=0.1)]

    pool = Pool(cpu_count())
    results = pool.map(worker, cartesian(selections, mutations))
    pool.close()

    x, labels = 0, []
    for res in results:
        max, min, avg, std, label = res
        plt.bar(x, height=max-min, width=0.05, bottom=min, color='blue', zorder=3)
        plt.bar(x, height=std, width=0.4, bottom=avg-std/2, color='blue', zorder=3)
        labels.append(label)
        x += 1

    plt.grid(zorder=0)
    plt.xticks(range(len(labels)), labels, rotation=90)
    plt.ylabel('Fitness')
    plt.title('Combinations comparison')

    plt.show()

if __name__ == '__main__':
    permutation_compare()