from genericpath import exists
import pygame
import pygame_gui
import random
import time
import numpy as np
import json

from eight_game_runner import EightGameRunner

DEFAULT_GRID = [1, 2, 3, 4, 5, 6, 7, 8, 0]

BABY_BLUE = 191, 215, 237
NAVY_BLUE = 0, 59, 115
WHITE = 255, 255, 255
BLACK = 0, 0, 0

SCREEN_SIZE = (1280, 720)

circle = pygame.image.load('circle_emoji.png')
up = pygame.image.load('up.png')
down = pygame.image.load('down.png')
left = pygame.image.load('left.png')
right = pygame.image.load('right.png')
circle = pygame.transform.scale(circle, (80, 80))
up = pygame.transform.scale(up, (80, 80))
down = pygame.transform.scale(down, (80, 80))
left = pygame.transform.scale(left, (80, 80))
right = pygame.transform.scale(right, (80, 80))
moves_emojis = {'': circle, 'f': up, 'b': down, 'l': left, 'r': right}

pygame.init()
font = pygame.font.Font('Google Sans Text Medium.ttf', 40)
title = font.render('8 digit Puzzle', True, NAVY_BLUE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("8 Puzzle")
background = pygame.Surface(SCREEN_SIZE)
background.fill(pygame.Color(BABY_BLUE))
manager = pygame_gui.UIManager(SCREEN_SIZE, 'theme.json')

# Botones (Resolver & Random)
solve_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 600), (350, 70)),
                                            text='Solve',
                                            manager=manager,
                                            object_id="#solve_btn")
random_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((135, 600), (350, 70)),
                                             text='Random',
                                             manager=manager,
                                             object_id="#solve_btn")

# Busqueda (label & dropdown)
dropdown_layout_rect = pygame.Rect((850, 150), (280, 60))
algorithmOptions = ["bpp", "bpa", "bppv",
                    "heu_local", "heu_global", "heu_weighted"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[0],
                                                       relative_rect=dropdown_layout_rect,
                                                       manager=manager)
pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Search: ",
                                     relative_rect=pygame.Rect((620, 150), (280, 60)))

# Heuristica (label & dropdown)
dropdown_layout_rect2 = pygame.Rect((850, 270), (280, 60))
heuristicsOptions = ["Manhattan Distance",
                     "Misplaced Tiles", "Cuadratic Manhattan"]
heuristicsDropDown = pygame_gui.elements.UIDropDownMenu(options_list=heuristicsOptions,
                                                        starting_option=heuristicsOptions[0],
                                                        relative_rect=dropdown_layout_rect2,
                                                        manager=manager)
heuristicsLabel = pygame_gui.elements.ui_label.UILabel(parent_element=heuristicsDropDown,
                                                       manager=manager,
                                                       text="Heuristic: ",
                                                       relative_rect=pygame.Rect((620, 270), (280, 60)))

def state_to_matrix(state):
    res = []
    for i in state.keys():
        res.append(state[i])
    return np.reshape(res, (3, 3))

def initial_grid(): 
    c = json.loads(open('conf.json', 'r').read())
    ret = {}
    ret['move'] = ''
    ret['state'] = np.reshape(c['eight_game']['initialGrid'], (3,3))
    return ret

def solve(grid, config):
    conf = json.loads(open('conf.json', 'r').read())
    conf['searchMethod'] = config['algorithm']
    conf['heuristic'] = config['heuristic']
    flatarray = []
    for i in range(3):
        for j in range(3):
            flatarray.append(grid['state'][i][j])
    print(flatarray)
    conf['initialGrid'] = conf['eight_game']['initialGrid']
    conf['goalGrid'] = conf['eight_game']['goalGrid']

    result = EightGameRunner(conf).run()
    vals = []
    if 'solution' in result:
        for grid in result['solution']:
            val = {}
            val['move'] = grid['move']
            val['state'] = state_to_matrix(grid['state'])
            vals.append(val)
        animate(vals)

    report_msg = '<b>Result: </b>'+result['status']+'<br/><b>Depth:</b>'+str(result['depth'])+'<br/><b>Cost:</b>'+str(result['cost'])+ \
        '<br/><b>Expanded nodes:</b>'+str(result['expandedNodes'])+'<br/><b>Frontier nodes:</b>' + \
        str(result['frontierNodes'])+'<br/><b>Time:</b>'+str(result['processingTime'])+'seconds'
    confirmation_win = pygame_gui.windows.ui_confirmation_dialog.UIConfirmationDialog(rect=pygame.Rect((600, 300), (180, 80)),
                                                                                      manager=manager,
                                                                                      action_long_desc=report_msg,
                                                                                      window_title=' Search Report',
                                                                                      )
    if not vals:
        return initial_grid()
    else:
        return vals[-1]

def display(grid):
    for i in range(3):
        for j in range(3):
            rect = pygame.Rect(i*15 + (i+1)*120, j*15 +
                               (j)*120 + 150, 120, 120)
            pygame.draw.rect(screen, NAVY_BLUE, rect)
            if grid['state'][j][i] == 0:
                screen.blit(moves_emojis[grid['move']],
                            (rect.left+20, rect.top+20))
            else:
                textSurf = font.render(str(grid['state'][j][i]), True, WHITE)
                textRect = textSurf.get_rect()
                textRect.center = rect.left+60, rect.top+60
                screen.blit(textSurf, textRect)
    pygame.display.update()


def animate(grids):
    for grid in grids:
        display(grid)
        time.sleep(1)


screen.blit(background, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
algorithm = algorithmOptions[0]
heuristic = None
# ret = [
#     {
#         'move': '',
#         'state': [[1, 2, 3], [5, 6, 0], [4, 7, 8]]
#     },
#     {
#         'move': 'r',
#         'state': [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
#     },
#     {
#         'move': 'r',
#         'state': [[1, 2, 3], [0, 5, 6], [4, 7, 8]]
#     },
#     {
#         'move': 'u',
#         'state': [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
#     },
#     {
#         'move': 'l',
#         'state': [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
#     },
#     {
#         'move': 'l',
#         'state': [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#     }
# ]
# grid = ret[0]


grid = initial_grid()
print(grid)

def randomize():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(a)
    grid_displayed = np.reshape(a, (3, 3))
    random_grid = {
        'move': '',
        'state': grid_displayed
    }
    display(random_grid)
    time.sleep(1)
    return random_grid


crashed = False
while not crashed:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == solve_button:
                    grid = solve(
                        grid, {'algorithm': algorithm, 'heuristic': heuristic})
                elif event.ui_element == random_button:
                    grid = randomize()

            elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == algorithmDropDown:
                    algorithm = event.text
                elif event.ui_element == heuristicsDropDown:
                    heuristic = event.text
        manager.process_events(event)

    if (algorithm == "BPA" or algorithm == "BPP" or algorithm == "BPPV"):
        heuristicsDropDown.hide()
        heuristicsLabel.hide()
        # heuristicsLabel._visible(False)
    else:
        heuristicsDropDown.show()
        heuristicsLabel.show()

    manager.update(time_delta)
    screen.blit(background, (0, 0))
    screen.blit(title, (350, 35))
    manager.draw_ui(screen)

    display(grid)
    pygame.display.update()
