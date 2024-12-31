import pygame
import pprint
from board import Board
from board import Token
pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width))
screen_center = [screen.get_width()/2,screen.get_height()/2]


board_surface = pygame.Surface((800,800))
new_board = Board(screen_center, 100)

new_token = Token(new_board.grid_size[0], (300,300))


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    for row in new_board.rows:
        row.draw_cells(screen)
        
    for row in new_board.rows:
        row.draw_line(screen)


    #pygame.draw.circle(screen,(255,0,0),pygame.mouse.get_pos(), 30)
    
    new_token.draw_self(screen)
    new_token.is_held()
    

    pygame.display.flip()

pygame.quit()
