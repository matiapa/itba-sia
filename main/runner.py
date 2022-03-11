from main.informed_solvers import *
from main.uninformed_solvers import *
from main.visualization import *
import json
import timeit

class Runner:

  """
  El game runner puede overridear este método y leer configuraciones adicionales.
  Si tiene heurísticas, debe cargar la heurística seleccionada en self.HEURISTIC
  """
  def read_config(self):
    conf = json.loads(open('conf.json', 'r').read())
    self.SEARCH_METHOD = conf['searchMethod']
    self.BPPV_START_LIMIT = conf['bppvStartLimit']
    self.HEU_WEIGHT = conf['heu_weight']
    self.PLOT_DECISION_TREE = conf['plotDecisionTree']
    self.SEARCH_TIMEOUT = conf['timeout']

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
    if self.SEARCH_METHOD == 'bpa':
      self.solver = SolverBPA(gs)
    elif self.SEARCH_METHOD == 'bpp':
      self.solver = SolverBPP(gs) 
    elif self.SEARCH_METHOD == 'bppv':
      self.solver = SolverBPPV(gs, self.BPPV_START_LIMIT)
    elif self.SEARCH_METHOD == 'heu_local':
      self.solver = SolverLocalHeuristic(gs, heuristics[self.HEURISTIC])
    elif self.SEARCH_METHOD == 'heu_global':
      self.solver = SolverGlobalHeuristic(gs, heuristics[self.HEURISTIC])
    elif self.SEARCH_METHOD == 'heu_weighted':
      self.solver = SolverWeightHeuristic(gs, heuristics[self.HEURISTIC], self.HEU_WEIGHT)
    else:
      print(f"Unknown search method: {self.SEARCH_METHOD}")
      exit(-1)

    # Mostramos los parámetros de la búsqueda

    print("> Search parameters")
    print(f"-  Search method: {self.SEARCH_METHOD}")
    if self.SEARCH_METHOD == 'bppv':
      print(f"-  Initial depth limit: {self.BPPV_START_LIMIT}")
    elif 'heu' in self.SEARCH_METHOD:
      print(f"-  Heuristic: {self.HEURISTIC}")
      if self.SEARCH_METHOD == 'heu_weighted':
        print(f"-  Weight: {self.HEU_WEIGHT}")

  """
  Este es el método que se debe ejecutar para buscar una solución y
  posteriormente visualizar los resultados
  """
  def run(self):
    # Leemos la configuración y creamos el estado inicial

    self.read_config()

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
      while not solved and (elapsed_time <= self.SEARCH_TIMEOUT or self.SEARCH_TIMEOUT < 0):
        n, solved = next(iterator)
        elapsed_time = timeit.default_timer() - start_time
      if not solved:
        failure_reason = 'Run out of time'
    except StopIteration:
      failure_reason = 'No more frontier nodes'

    # Mostramos el resultado

    if solved:
      print("\n> Solution found")
      print(f"-  Depth: {n.depth}")
      print(f"-  Cost: {n.cost}")
      print(f"-  Expanded nodes: {len(self.solver.explored)}")
      print(f"-  Frontier nodes: {len(self.solver.frontier)}")
    else:
      print("\n> Solution not found")
      print(f"\n-  Failure reason: {failure_reason}")
    print(f"-  Processing time: {elapsed_time} ms")

    if solved:
      print("\n> Generating solution graph...")
      renderBranch(n)
      print("-  Graph generated at out/solution_branch.pdf")

    if self.PLOT_DECISION_TREE:
      print("\n> Generating decision tree graph...")
      renderTree(self.solver.initial_node)
      print("-  Graph generated at out/decision_tree.pdf")