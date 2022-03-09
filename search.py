import copy
import json
import graphviz

conf = json.loads(open('conf.json', 'r').read())

GRID_SIZE = conf['gridSize']
INITIAL_GRID = conf['initialGrid']
GOAL_GRIDS = conf['goalGrids']
SEARCH_METHOD = conf['searchMethod']
BPPL_LIMIT = conf['bpplLimit']
PLOT_DECISION_TREE = conf['plotDecisionTree']

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
        return type(other) is Node and self.grid == other.grid


def node_label(node):
    str = ''
    for i in range(0, GRID_SIZE):
        for j in range(0, GRID_SIZE):
            str += f'{node.grid[i][j]} '
        str += '\n'
    return str


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

def uninformed_search(root):
    frontier_nodes = [root]
    expanded_nodes = []
  
    while(len(frontier_nodes) > 0):
        # Quitamos el nodo de la cola
        node = frontier_nodes.pop(0)

        # Ponemos una profundidad límite
        if SEARCH_METHOD == "BPPL" and node.depth > (BPPL_LIMIT - 1):
            continue

        # Validamos si es un nodo solución
        if node.grid in GOAL_GRIDS:
            return node

        # Como no es solución, lo expandimos
        expanded_nodes.append(node)
        expand_node(node, frontier_nodes, expanded_nodes)
        
        # Reordenamos los nodos frontera de menor a mayor profundidad (BPA)
        if SEARCH_METHOD == "BPA":
            frontier_nodes.sort(key = lambda node : node.depth)
        elif SEARCH_METHOD == "BPP" or SEARCH_METHOD == "BPPL":
            frontier_nodes.sort(key = lambda node : node.depth, reverse=True)
        else:
            print(f'Unknown search method: {SEARCH_METHOD}')
            exit(-1)
        
    # No se encontró ninguna solución
    return None

# ---------------------------------------------------------------------

def build_graphviz_tree(node, graph):
    graph.node(str(node.id), node_label(node))
    
    for child in node.childs:
        build_graphviz_tree(child, graph)
        graph.edge(str(node.id), str(child.id))

def build_graphviz_branch(node, graph):
    graph.node(str(node.id), node_label(node))

    if node.parent != None:
        build_graphviz_branch(node.parent, graph)
        graph.edge(str(node.parent.id), str(node.id))

def renderTree(root):
    graph = graphviz.Digraph('Decision tree')
    build_graphviz_tree(root, graph)
    graph.render(directory='out', view=True)

def renderBranch(leaf):
    graph = graphviz.Digraph('Solution branch')
    build_graphviz_branch(leaf, graph)
    graph.render(directory='out', view=True)

# ---------------------------------------------------------------------

# Crear nodo inicial

root = Node(INITIAL_GRID, None, 0)
solution_node = uninformed_search(root)

if solution_node != None:
    print("Solution found!")
    renderBranch(solution_node)
else:
    print("Solution not found")

if PLOT_DECISION_TREE:
    renderTree(root)