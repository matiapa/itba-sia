from main.crossing.multiple_cross import MultipleCross
from main.individual import Individual, IndividualFactory
from main.crossing.cross import Cross

from typing import List, Tuple
import numpy as np


class SimpleCross(MultipleCross):

    def __str__(self):
        return "SimpleCross"

    def __init__(self):
        super().__init__(1)