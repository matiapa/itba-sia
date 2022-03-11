class GameState():

  """ Devuelve verdadero si el estado es objetivo/ganador"""
  @property
  def isobjective(self):
    raise 'Not implemented exception'

  """
  Devuelve un diccionario cuyas claves son strings que representan los movimientos posibles
  según las reglas del juego, y cuyos valores son los costos asociados a los movimientos
  """
  @property
  def game_moves(self):
    raise 'Not implemented exception'

  """
  Ejecuta un movimiento en el juego. De ser válido, devuelve un nuevo estado con dicho movimiento ejecutado
  """
  def make_move(self, m: str):
    raise 'Not implemented exception'

  """
  Todo juego debe poder mostrarse en pantalla, aunque sea una representación muy básica
  """
  def __str__(self): 
    raise 'Not implemented exception'

  """
  Todo juego debe poder devolver un conjunto de pares con informacion del estado interno del mismo
  """
  @property
  def data(self): 
    raise 'Not implemented exception'

  """
  Todo estado debe tener un hash debido a que será almacenado en un set
  """
  def __hash__(self): 
    raise 'Not implemented exception'

  """
  Todo estado debe definir la igualdad ya que se usará para evitar estados repetidos
  """
  def __eq__(self, o): 
    raise 'Not implemented exception'