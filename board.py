import pygame
import pprint

class Board:
    
    GRID_NUMBER = 8
    
    def __init__(self, x, y, grid_size=100):
        
        self.grid_size = (grid_size, grid_size)
        self.size = ( self.grid_size[0]*Board.GRID_NUMBER , self.grid_size[0]*Board.GRID_NUMBER )
        self.x = x
        self.y = y
        self.center = ( x+self.size[0]/2 , y+self.size[1]/2 )
        self.__rows = []
        
        for row in range(Board.GRID_NUMBER):
            new_row = Row(row*self.grid_size[1], self.grid_size)
            self.__rows.append(new_row)
            
        self.rows = tuple(self.__rows)
        
    
        
class Row:
    def __init__(self, y, size):
        self.x = 0
        self.y = y
        self.__cells = []
        self.size = size
        
        for cell in range(8):
            new_cell = pygame.Rect(self.x+cell*size[0],self.y,self.size[0],self.size[1])
            self.__cells.append(new_cell)
            
        self.cells = tuple(self.__cells)
        
    def draw_cells(self, surface):
        for row_index, cell in enumerate(self.cells):
            if (row_index + (self.x // self.size[0])) % 2 == 0:
                color = pygame.Color("Azure1")  # Light color
            else:
                color = pygame.Color("gray16")
            pygame.draw.rect(surface, color, cell,)  # Drawing the cell with a red outline (2 is the width of the outline)

            
        
        


