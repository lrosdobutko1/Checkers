import pygame
import pprint
from board import Board
from board import Token
pygame.init()

white = (255, 255, 255)

display_info = pygame.display.Info()
screen_width = display_info.current_h*0.9
screen = pygame.display.set_mode((screen_width, screen_width))
screen_center = [screen.get_width()/2,screen.get_height()/2]

# Font for displaying the counter
font = pygame.font.Font(None, 36)  # Default font, size 36

# Clock for controlling the frame rate
clock = pygame.time.Clock()
fps = 100  # Refresh rateboard_surface = pygame.Surface((800,800))
frame_counter = 0 # Frame counter

new_board = Board(screen_center, 100)

new_token = Token(new_board.grid_size[0], (300,300))


# Main game loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if new_token.mouse_distance < new_token.radius:
            print("mouse down")                    
            if pygame.mouse.get_pressed()[0]:
                new_token.center = new_token.mouse_pos

        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse up")
            for cell in new_token.move_list:
                if pygame.math.Vector2(new_token.center).distance_to(cell.center) <= new_token.radius:
                    new_token.center = cell.center

    #game logic
    frame_counter += 1
    if frame_counter >= 100:
        frame_counter = 0
        
    #new_token.check_if_held()
    #draw screen elements
    screen.fill((0, 0, 0))

    #draw the board
    for row in new_board.rows:
        row.draw_cells(screen)
    
    #draw tokens
    new_token.draw_self(screen)
    new_token.get_move_list(new_board)
    for line in new_token.move_list:
        pygame.draw.line(screen,(255,0,255),new_token.center,line.center, 3)

    
    #draw frame counter
    counter_text = font.render(f"Frame: {frame_counter}", True, white)
    screen.blit(counter_text, (10, 10))  # Draw text at top-left corner
    

    pygame.display.flip()
    
    clock.tick(100)

pygame.quit()
