import pygame
import board
pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width))

# Set up the main screen
screen = pygame.display.set_mode((screen_width, screen_width))
screen_center = [screen.get_width()/2,screen.get_height()/2]

board_cell_color = pygame.Color("grey")  
board_cell_size = 100,100

board_width = board_cell_size[0]*8
board_height = board_cell_size[1]*8
board_surface = pygame.Surface((board_width, board_height))  
board_surface_center = [board_surface.get_width()/2, board_surface.get_width()/2]
board_surface.fill((0, 0, 255))  # Blue background for the board


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    screen.blit(board_surface, (screen_center[0]-(board_width/2), (screen_center[1]-board_height/2)))
    
    
    pygame.display.flip()

pygame.quit()
