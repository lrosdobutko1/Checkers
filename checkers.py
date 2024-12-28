import pygame
import pprint
from board import Board
from board import Row

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width))
screen_center = [screen.get_width()/2,screen.get_height()/2]

new_board = Board(100,100,100)

pprint.pprint(new_board.rows[3].cells)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    # for row in new_board.rows:
    #     for cell in row.cells:
    #         pygame.draw.rect(screen, (255, 0, 0), cell, 1)  # Drawing the cell with a red outline (2 is the width of the outline)

    for row in new_board.rows:
        row.draw_cells(screen)
        
    pygame.draw.circle(screen,(255,0,0),pygame.mouse.get_pos(), 30)
    
    pygame.display.flip()

pygame.quit()
