import pygame

pygame.init()

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width))
print(screen.get_size())

# Set up the main screen
screen = pygame.display.set_mode((screen_width, screen_width))

board_cell_color = pygame.Color("grey")  
board_cell_size = pygame.Rect((0,0),(100,100)) 

board_width = screen_width/2
board_surface = pygame.Surface((board_width, board_width))  
board_surface.fill((0, 0, 255))  # Blue background for the board



# Draw the smaller rectangle inside the board surface
pygame.draw.rect(board_surface, board_cell_color, board_cell_size)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    screen.blit(board_surface, (screen_width/4, screen_width/4))

    pygame.display.flip()

pygame.quit()
