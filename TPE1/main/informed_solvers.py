from main.game_state import GameState
from main.solver import Solver
from main.node import Node
from heapq import *

class SolverHeuristic(Solver): 
  
  def __init__(self, game_state: GameState, heuristic):
    self.h = heuristic
    super().__init__(game_state)

  def score(self, node): 
    return node.heuristic

  def new_node(self, new_state, parent, depth, cost, src_action):
    n = self.HeuristicNode(new_state, parent, parent.depth+1 if parent != None else 0, cost, src_action, self.h(new_state))
    return n

  class HeuristicNode(Node):

    def __init__(self, state, n, depth, cost, src_action, heuristic):
      super().__init__(state, n, depth, cost, src_action)
      self.heuristic = heuristic

class SolverLocalHeuristic(SolverHeuristic):

  def __init__(self, game_state: GameState, heuristic):
    super().__init__(game_state, heuristic)

  def push_to_heap(self, node):
    heappush(self.frontier, ( -node.depth, self.score(node), node.id, node))

class SolverGlobalHeuristic(SolverHeuristic):

  def __init__(self, game_state: GameState, heuristic):
    super().__init__(game_state, heuristic)
  
  def push_to_heap(self, node):
    heappush(self.frontier, (self.score(node), node.id, node))

class SolverWeightHeuristic(SolverHeuristic):
  
  def __init__(self, game_state: GameState, heuristic, w):
    super().__init__(game_state, heuristic)
    self.w = w

  def score(self, node): 
    return node.heuristic * self.w + node.cost * (1-self.w)
    
  def push_to_heap(self, node):
    heappush(self.frontier, (self.score(node), node.id, node))