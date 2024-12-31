
import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

# Object (a rectangle)
object_rect = pygame.Rect(300, 200, 100, 100)  # x, y, width, height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse collides with the rectangle
    if object_rect.collidepoint(mouse_pos):
        color = red  # Change color to red when colliding
    else:
        color = blue  # Default color is blue

    # Draw everything
    screen.fill(white)
    pygame.draw.rect(screen, color, object_rect)

    pygame.display.flip()

pygame.quit()