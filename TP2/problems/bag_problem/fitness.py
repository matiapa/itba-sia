from typing import Dict, List
from individual import BagIndividual
from main.fitness import Fitness

class BagFitness(Fitness):

    __cache: Dict[str, float] = {}

    max_weight: int
    weights: List[int] = []
    benefits: List[int] = []

    def __init__(self) -> None:
        f = open("in/config.txt", "r")
        
        header = f.readline()
        self.max_weight = int(header.split(' ')[1])

        for line in f.readlines():
            benefit, weight = line.split(' ')
            self.benefits.append(int(benefit))
            self.weights.append(int(weight))

        f.close()        

    def apply(self, individual: BagIndividual) -> float:
        key = str(individual.genes)

        if key not in self.__cache:
            weight_sum = 0
            benefit_sum = 0

            for i in range(0, len(individual.genes)):
                if individual.genes[i] == 1:
                    weight_sum += self.weights[i]
                    benefit_sum += self.benefits[i]

            if weight_sum <= self.max_weight:
                self.__cache[key] = benefit_sum
            else:
                self.__cache[key] = 1/weight_sum

        return self.__cache[key]