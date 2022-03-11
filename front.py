import pygame
import pygame_gui

BABY_BLUE = 191, 215, 237
NAVY_BLUE = 0, 59, 115
WHITE = 255,255,255
BLACK = 0,0,0

SCREEN_SIZE = (1280, 720)

pygame.init()
font = pygame.font.Font('Google Sans Text Medium.ttf',40)
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
algorithmOptions = ["BPA", "BPP", "BPPV", "Heuristica Local", "Heuristica Global","A*"]
algorithmDropDown = pygame_gui.elements.UIDropDownMenu(options_list=algorithmOptions,
                                                       starting_option=algorithmOptions[1],
                                                       relative_rect=dropdown_layout_rect,
                                                       manager=manager)
pygame_gui.elements.ui_label.UILabel(parent_element=algorithmDropDown,
                                     manager=manager,
                                     text="Search: ",
                                     relative_rect=pygame.Rect((620, 150), (280, 60)))

# Heuristica (label & dropdown)                   
dropdown_layout_rect2 = pygame.Rect((850, 270), (280, 60))            
heuristicsOptions = ["Manhattan Distance", "Misplaced Tiles", "Cuadratic Manhattan"]
heuristicsDropDown = pygame_gui.elements.UIDropDownMenu(options_list=heuristicsOptions,
                                                       starting_option=heuristicsOptions[1],
                                                       relative_rect=dropdown_layout_rect2,
                                                       manager=manager)
pygame_gui.elements.ui_label.UILabel(parent_element=heuristicsDropDown,
                                     manager=manager,
                                     text="Heuristic: ",
                                     relative_rect=pygame.Rect((620, 270), (280, 60)))

def draw_blocks():
    for i in range(3):
        for j in range(3):
            rect = pygame.Rect(i*15 + (i+1)*120, j*15 + (j)*120 + 150, 120, 120)
            pygame.draw.rect(screen, NAVY_BLUE, rect)
            textSurf = font.render(str(i*3+j), True, WHITE)
            textRect = textSurf.get_rect()
            textRect.center = rect.left+60, rect.top+60
            screen.blit(textSurf, textRect)

screen.blit(background, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()

crashed = False
while not crashed:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        manager.process_events(event)
    
        
    manager.update(time_delta)
    screen.blit(background, (0, 0))
    screen.blit(title, (350, 35))
    manager.draw_ui(screen)
    draw_blocks()
    pygame.display.update()
