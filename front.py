import pygame
import pygame_gui

BABY_BLUE = 191, 215, 237
NAVY_BLUE = 0, 59, 115
WHITE = 255,255,255
BLACK = 0,0,0

SCREEN_SIZE = (1280, 720)

pygame.init()
font = pygame.font.Font('Google Sans Text Medium.ttf',40)
title = font.render('Rompecabezas de 8 dígitos', True, NAVY_BLUE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("8 Puzzle")
background = pygame.Surface(SCREEN_SIZE)
background.fill(pygame.Color(BABY_BLUE))
manager = pygame_gui.UIManager(SCREEN_SIZE, 'theme.json')

# pygame_gui.elements.ui_label.UILabel(manager=manager,
#                                         text="Rompecabezas de 8 dígitos",
#                                         relative_rect=pygame.Rect((500, 10), (300, 70)),
#                                         object_id="#title_box"
#                                         )

def draw_blocks():
    for i in range(3):
        # if block['block'] != 0:
        for j in range(3):
            rect = pygame.Rect(i*15 + (i+1)*120, j*15 + (j)*120 + 150, 120, 120)
            pygame.draw.rect(screen, NAVY_BLUE, rect)
            textSurf = font.render(str(i*3+j), True, WHITE)
            textRect = textSurf.get_rect()
            textRect.center = rect.left+60, rect.top+60
            screen.blit(textSurf, textRect)
            # else:
            #     pygame.draw.rect(screen, WHITE, pygame.Rect(30, 30, 60, 60))

screen.blit(background, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
# puzzle = Puzzle.new(250, 220, 330, 330)
# puzzle.initialize()

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
    blocks = {}
    draw_blocks()
    pygame.display.update()
