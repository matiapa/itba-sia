# TODO: podriamos aprender a hacerla inmutable 
from game_state import GameState
import copy
import numpy as np

class EightGameState(GameState):

  offsets = {'f':-3 , 'b':3 , 'l':-1 , 'r':1}
  goal_table = None

  def __init__(self, **kwargs):
    self.table = kwargs.get('table', EightGameState.__new_table()) # TODO: deberia ser una tupla
    self.zero = kwargs.get('target', self.table.index(0))
    self.__swap(self, self.zero, kwargs.get('source', self.zero)) 

  @staticmethod
  def __new_table():
    x = np.arange(9)
    np.random.shuffle(x)
    return x.tolist()  

  @staticmethod 
  def __swap(self, n, z):
      self.table[n], self.table[z] = self.table[z], self.table[n]

  @staticmethod
  def setGoalTable(table):
    EightGameState.goal_table = table

  @property 
  def matrix(self): 
    return np.reshape(self.table, (3, 3))

  @property
  def isobjective(self):
    return self.table == EightGameState.goal_table

  def make_move(self, m: str):
    if m not in self.offsets.keys():
      raise 'Invalid move code'

    if (m == 'f' and self.zero < 3) \
      or (m == 'b' and self.zero >= 6) \
      or (m == 'l' and self.zero % 3 == 0 ) \
      or (m == 'r' and self.zero % 3 == 2 ):  
        return None   
    
    new_zero = self.zero + self.offsets[m]
    return EightGameState(table=copy.deepcopy(self.table), source=self.zero, target=new_zero)

  def __hash__(self): 
    return hash(tuple(self.table))

  def __eq__(self, o): 
    return isinstance(o, EightGameState) and o.table == self.table

  @property
  def game_moves(self):
    return {'b': 1, 'f': 1, 'l': 1, 'r': 1}

  def __str__(self): 
    return str(np.reshape(self.table, (3, 3)))

  @property
  def data(self):
    d = {} 
    for pos in range(9): 
      d[str(pos+1)] = self.table[pos]
    return d