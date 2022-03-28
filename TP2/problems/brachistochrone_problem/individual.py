from main.individual import Individual, IndividualFactory
from typing import List
import numpy as np 

class BrachistochroneIndividual(Individual):

    genome_size: int
    angle_limit = 0.01
    h0 = 1
    hf = 0
    horizontal_length = 10
    q_control_points = 100
    step = 0

    def __init__(self, genes):
        BrachistochroneIndividual.step = BrachistochroneIndividual.horizontal_length / (BrachistochroneIndividual.q_control_points + 1)
        super().__init__(genes) 



    @staticmethod
    def genome_size() -> int:
        return BrachistochroneIndividual.q_control_points

    def _initialize_genes(self) -> List[float]:
        return [ (2*np.pi/2) * x -  ( np.pi/2) for x in  np.random.rand(1)]+[ (2*BrachistochroneIndividual.angle_limit) * x -  ( BrachistochroneIndividual.angle_limit) for x in  np.random.rand(BrachistochroneIndividual.q_control_points-1)] # TODO !! que onda ese -1 

    def __str__(self) -> str:
        return str(sum(self.genes))

class BrachistochroneIndividualFactory(IndividualFactory):

    def instantiate(self, genes: List[float]) -> Individual:
        return BrachistochroneIndividual(genes)