from typing import List
from individual import BagIndividual
from main.fitness import Fitness
from main.stop_criteria import StopCriteria

class BagStopCriteria(StopCriteria):

    def should_stop(self, population: List[BagIndividual], fitness: Fitness, generation: int) -> bool:
        return generation > 100