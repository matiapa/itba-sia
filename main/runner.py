from main.informed_solvers import *
from main.uninformed_solvers import *
from main.visualization import *
import timeit

class Runner:

  """
  Recibe un parámetro con configuraciones sobre la búsqueda y el juego
  """
  def __init__(self, config):
    self.config = config

  """
  El game runner debe retornar un estado inicial para su juego
  """
  def create_initial_state(self):
    raise 'Method not implemented'

  """
  El game runner debe retornar un diccionario cuyas claves sean los nombres de las heurísticas
  que posee y sus valores las funciones de las mismas. Si no tiene heurísticas, retornarlo vacío
  """
  def get_heuristics(self):
    raise 'Method not implemented'

  """
  Este método aplica las configuraciones y valores obtenidos previamente para generar la
  instancia apropiada de una clase Solver
  """
  def prepare_solver(self, gs):
    heuristics = self.get_heuristics()

    self.solver = None
    if self.config['searchMethod'] == 'bpa':
      self.solver = SolverBPA(gs)
    elif self.config['searchMethod'] == 'bpp':
      self.solver = SolverBPP(gs) 
    elif self.config['searchMethod'] == 'bppv':
      self.solver = SolverBPPV(gs, self.config['bppvStartLimit'])
    elif self.config['searchMethod'] == 'heu_local':
      self.solver = SolverLocalHeuristic(gs, heuristics[self.config['heuristic']])
    elif self.config['searchMethod'] == 'heu_global':
      self.solver = SolverGlobalHeuristic(gs, heuristics[self.config['heuristic']])
    elif self.config['searchMethod'] == 'heu_weighted':
      self.solver = SolverWeightHeuristic(gs, heuristics[self.config['heuristic']], self.config['heuWeight'])
    else:
      print(f"Unknown search method: {self.config['searchMethod']}")
      exit(-1)

    # Mostramos los parámetros de la búsqueda

    print("> Search parameters")
    print(f"-  Search method: {self.config['searchMethod']}")
    if self.config['searchMethod'] == 'bppv':
      print(f"-  Initial depth limit: {self.config['bppvStartLimit']}")
    elif 'heu' in self.config['searchMethod']:
      print(f"-  Heuristic: {self.config['heuristic']}")
      if self.config['searchMethod'] == 'heu_weighted':
        print(f"-  Weight: {self.config['heuWeight']}")

  """
  Este es el método que se debe ejecutar para buscar una solución y
  posteriormente visualizar los resultados.
  """
  def run(self):
    # Leemos la configuración y creamos el estado inicial

    gs = self.create_initial_state()

    # Peparamos el solver a utilizar

    self.prepare_solver(gs)

    # Comenzamos la iteración

    print(f"\n> Searching solution...")

    iterator = iter(self.solver)
    solved = False
    failure_reason = ''
    n = None

    start_time = timeit.default_timer()
    elapsed_time = 0

    try:
      # for i in range(0,5):
      while not solved and ('searchTimeout' not in self.config or elapsed_time <= self.config['searchTimeout']):
        n, solved = next(iterator)
        elapsed_time = timeit.default_timer() - start_time
      if not solved:
        failure_reason = 'Run out of time'
    except StopIteration:
      failure_reason = 'No more frontier nodes'

    # Mostramos el resultado

    result = {}

    if solved:
      result['status'] = 'success'
      result['depth'] = n.depth
      result['cost'] = n.cost
      result['expandedNodes'] = len(self.solver.explored)
      result['frontierNodes'] = len(self.solver.explored)

      print("\n> Solution found")
      print(f"-  Depth: {n.depth}")
      print(f"-  Cost: {n.cost}")
      print(f"-  Expanded nodes: {len(self.solver.explored)}")
      print(f"-  Frontier nodes: {len(self.solver.frontier)}")
    else:
      result['status'] = 'failed'
      result['reason'] = failure_reason

      print("\n> Solution not found")
      print(f"\n-  Failure reason: {failure_reason}")

    result['processingTime'] = elapsed_time
    print(f"-  Processing time: {elapsed_time} ms")

    try:
      result['solution'] = self.__get_solution_sequence(n)
      result['solution'].reverse()

      if solved:
        print("\n> Generating solution graph...")
        renderBranch(n)
        print("-  Graph generated at out/solution_branch.pdf")

      if self.config['plotDecisionTree']:
        print("\n> Generating decision tree graph...")
        renderTree(self.solver.initial_node)
        print("-  Graph generated at out/decision_tree.pdf")
    except RecursionError:
      print("-  Couldn't generate solution path, too many nodes")

    return result

  def __get_solution_sequence(self, node):
    sequence = [{'move': node.src_action, 'state': node.state.data}]

    if node.parent != None:
      sequence += self.__get_solution_sequence(node.parent)

    return sequence