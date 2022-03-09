import copy
import graphviz

GRID_SIZE = 3
INITIAL_GRID = [[8,3,5],[4,'x',1],[2,7,6]]
MAX_DEPTH = 3

class Node:

    LAST_ID = 0

    def __init__(self, grid, parent, depth):
        self.grid = grid
        self.childs = []
        self.parent = parent
        self.depth = depth
        self.id = Node.LAST_ID
        Node.LAST_ID += 1

    def __eq__(self, other):
        return self.grid == other.grid


def make_movement(node, i1, j1, i2, j2, expanded_nodes, frontier_nodes):
    # Creamos el nuevo nodo con el estado apropiado

    new_grid = copy.deepcopy(node.grid)
    temp = new_grid[i1][j1]
    new_grid[i1][j1] = new_grid[i2][j2]
    new_grid[i2][j2] = temp
    new_node = Node(new_grid, node, node.depth+1)

    # Si el estado no existía ya lo agregamos al árbol y al conjunto frontera

    if new_node not in expanded_nodes:
        node.childs.append(new_node)
        frontier_nodes.append(new_node)


def expand_node(node, frontier_nodes, expanded_nodes):
    # Exploramos todas las posibilidades

    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            if node.grid[i][j] == 'x':

                # Si hay una ficha arriba
                if i > 0:
                    make_movement(node, i-1, j, i, j, expanded_nodes, frontier_nodes)

                # Si hay una ficha abajo
                if i < 2:
                    make_movement(node, i+1, j, i, j, expanded_nodes, frontier_nodes)

                # Si hay una ficha a la izquierda
                if j > 0:
                    make_movement(node, i, j-1, i, j, expanded_nodes, frontier_nodes)

                # Si hay una ficha a la derecha
                if j < 2:
                    make_movement(node, i, j+1, i, j, expanded_nodes, frontier_nodes)

def is_node_solution(node):
    g = node.grid
    return g[0][0] == '1' and g[0][1] == '2' and g[0][2] == '3' \
        and g[1][0] == '4' and g[1][1] == '5' and g[1][2] == '6' \
            and g[2][0] == '7' and g[2][1] == '8' and g[1][2] == 'x'

def bfs(root):
    frontier_nodes = [root]
    expanded_nodes = []
  
    while(len(frontier_nodes) > 0):
        # Quitamos el nodo de la cola
        node = frontier_nodes.pop(0)

        # Ponemos una profundidad límite
        if node.depth > (MAX_DEPTH - 1):
            return None

        # Validamos si es un nodo solución
        if is_node_solution(node):
            return node

        # Como no es solución, lo expandimos
        expanded_nodes.append(node)
        expand_node(node, frontier_nodes, expanded_nodes)
        
        # Reordenamos los nodos frontera de menor a mayor profundidad (BPA)
        frontier_nodes.sort(key = lambda node : node.depth)
        
    # No se encontró ninguna solución
    return None


# Crear nodo inicial

root = Node(INITIAL_GRID, None, 0)
solution_node = bfs(root)
