import pygame
import pprint

class Board:
    
    GRID_NUMBER = 8
    
    def __init__(self, center: list, grid_size: int):
        
        self.grid_size = (grid_size, grid_size)
        self.size = ( self.grid_size[0]*Board.GRID_NUMBER , self.grid_size[0]*Board.GRID_NUMBER )
        self.x = (center[0] - ((grid_size*Board.GRID_NUMBER)/2))
        self.y = (center[1] - ((grid_size*Board.GRID_NUMBER)/2))
        self.center = center
        self.__rows = []
        
        for row in range(Board.GRID_NUMBER):
            new_row = Row(self.x, self.y + row*self.grid_size[1], self.grid_size)
            self.__rows.append(new_row)
            
        self.rows = tuple(self.__rows)
        
    
        
class Row:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.__cells = []
        self.size = size
        
        for cell in range(8):
            new_cell = pygame.Rect(self.x+cell*size[0],self.y,self.size[0],self.size[1])
            self.__cells.append(new_cell)
            
        self.cells = tuple(self.__cells)
        
    def draw_cells(self, surface):
        for row_index, cell in enumerate(self.cells):
            # Check if the cell is in an even or odd column
            if (row_index + (self.y // self.size[1])) % 2 == 0:
                color = pygame.Color("Azure1")  # Light color
            else:
                color = pygame.Color("gray16")  # Dark color
                
            # Draw the cell with the chosen color
            pygame.draw.rect(surface, color, cell)
            
    def draw_line(self, surface):
        # Loop through each cell and check the distance from its center to the mouse position
        for cell in self.cells:
            cell_center = cell.center  # Get the center of the cell
            mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
            
            # Calculate the distance from the center of the cell to the mouse position
            distance = pygame.math.Vector2(cell_center).distance_to(mouse_pos)
            
            # If the mouse is within 300 pixels of the cell center, draw a line
            if distance < 150 and distance > 50:
                # Draw a line from the cell center to the mouse position
                pygame.draw.line(surface, (255, 0, 255), cell_center, mouse_pos, 3)
