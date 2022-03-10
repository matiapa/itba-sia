from game_state import GameState
from node import Node
from heapq import *

class Solver():

    '''
      La funcion score es una funcion que 
      - dado un nodo representante de un estado del juego -
      permite  saber su puntaje. Mientras menor sea el puntaje, mejor. 
      El algoritmo selecciona al que menor valor de score tiene. 
      Si se quiere seleccionar al que mayor valor de score tenga, se lo puede multiplicar por -1
    '''
    def score(self, node): 
      raise 'Not implemented exception'

    def __init__(self, game_state: GameState):
      self.initial_state = game_state
      self.root = self.new_node(self.initial_state, None, 0, 0) 

    @property 
    def initial_node(self): 
      return self.root

    
    def __iter__(self):
      # self.iter_done = False 
      self.frontier = [] # La Frontera es un Heap (AKA Priority Queue). No tiene sentido agregar y ordenar a futuro, mantenelo ordenado
      self.explored = set() 
      heappush(self.frontier, (self.score(self.root), 0, self.root))
      return self

    ''' 
      En cada iteracion devuelve 
        Excepcion si no pudo encontrar solucion
        Un Nodo valido si encontro solucion
        None si sigue buscando 
      El iterador no se destruye al encontrar una solucion, va a seguir buscando y la hoja solucion muere ahi    
    '''
    def __next__(self):

      self.check_frontier()
      n = heappop(self.frontier)[-1]
      self.mark_explored(n)

      if n.state.isobjective: 
        return n, True  
      
      game_moves = n.game_state.game_moves
      for m in game_moves.keys(): 
        new_state = n.game_state.make_move(m)
        if new_state is not None:
          node = self.new_node(new_state, n, n.depth + 1, n.cost + game_moves[m])
          if self.should_explore(node):  
            n.add(node) 
            self.push_to_heap(node)
    
      # print(n.game_state)
      return n, False

    def should_explore(self, node): 
      return node.game_state not in self.explored

    def new_node(self, new_state, parent, depth, cost):
      return Node(new_state, parent, parent.depth+1 if parent != None else 0, cost)

    def check_frontier(self):
      if len(self.frontier) == 0:  # TODO: aca podriamos aplicar lo de la profundidad en una extension del metodo
        raise StopIteration 
    
    def push_to_heap(self, node):
        heappush(self.frontier, (self.score(node), node.id, node)) # Le agrego el ID para romper desempates  # me esta siempre pusheando al heap 

    def mark_explored(self, n):
       n.mark_explored()
       self.explored.add(n.game_state) # como es un set, no pasa nada si ya estaba
