class GameState():

  """ Devuelve verdadero si el estado es objetivo/ganador"""
  @property
  def isobjective(self):
    raise 'Not implemented exception'

  """
  Devuelve un conjunto de strings representando movimientos posibles
  según las reglas del juego
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
    return 'Empty Game!'

  """
  Todo juego debe poder devolver un conjunto de pares con informacion del estado interno del mismo
  """
  @property
  def data(self): 
    raise 'Not implemented exception'