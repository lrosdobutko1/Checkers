import pygame

class BoardCell:
    def __init__(self, board_surface, size, color):
        
        self.board_surface = board_surface
        self.size = size
        self.color = color
        self.is_empty = True
        self.shape = pygame.Rect(0, 0, size)  # Smaller rectangle inside

        
    def draw_self(self):
        pygame.draw.rect(self.board_surface, self.color, self.shape)