import pygame

class BoardCell:
    def __init__(self, board_surface, rect, id):
        
        self.id = id
        self.board_surface = board_surface
        self.rect = rect
        self.occupied = False
        
    def draw_self(self, color):
        pygame.draw.rect(self.board_surface, color, self.rect)