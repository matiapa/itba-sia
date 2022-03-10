from solver import Solver
from game_state import GameState
from heapq import *

class SolverBPA(Solver): 
  def score(self, node): 
    return node.depth

class SolverBPP(Solver):  
  def score(self, node): 
    return -node.depth

class SolverBPPV(SolverBPP):
  # Considerar que pueden haber estados repetidos a distinta profundidad

  def __init__(self, game_state: GameState, start_limit: int):
    super().__init__(game_state)
    self.max_depth = start_limit

  def mark_explored(self, n):
    n.mark_explored()
    self.explored[n.game_state] = min(self.explored.get(n.game_state, n.depth), n.depth)

  def __iter__(self):
    x =  super().__iter__()
    self.explored = {}
    return x

  def should_explore(self, node):
    return node.game_state not in self.explored.keys() or self.explored[node.game_state] > node.depth

  def push_to_heap(self, node):
    heappush(self.frontier, ( int(node.depth / (self.max_depth + 1)), self.score(node), node.id, node)) # Le agrego el ID para romper desempates  # me esta siempre pusheando al heap
