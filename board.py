import pygame
import pprint

class Board:
    
    GRID_NUMBER = 8
    WHITE = (255,255,255)
    BLUE = (0,0,255)
    RED = (255,0,0)
    
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
        color = pygame.Color("Azure1")
        for row_index, cell in enumerate(self.cells):
            # Check if the cell is in an even or odd column
            if (row_index + (self.y // self.size[1])) % 2 == 0:
                color = pygame.Color("Azure1")  # Light color
            else:
                color = pygame.Color("gray16")  # Dark color
                
            # Draw the cell with the chosen color
            pygame.draw.rect(surface, color, cell)
            

class Token:
    def __init__(self, radius, center):
        self.radius = (radius/2) * 0.8
        self.center = center
        self.is_king = False
        self.player = 1
        self.legal_moves = []
        self.move_list = []
        self.valid_states = ["placed", "moving", "held"]
        self.state = self.valid_states[0]
        self.mouse_pos = (0,0)
        self.mouse_distance = 0
        self.cell_picker = pygame.Rect((self.center[0]-100,self.center[1]-100), (200,200))
        
    def draw_self(self, surface):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_distance = pygame.math.Vector2(self.center).distance_to(self.mouse_pos)
        color = Board.RED
        
        if self.mouse_distance < self.radius:
            color = Board.BLUE
        else:
            color = Board.RED
            
        self.cell_picker = pygame.Rect((self.center[0]-100,self.center[1]-100), (200,200))
           
        pygame.draw.circle(surface,color,self.center, self.radius)
        
    def get_move_list(self, board):
        self.move_list = []
        
        for row in board.rows:
            for cell in row.cells:
                cell_center = cell.center
                move1 = 0
                move2 = 0
                move3 = 0
                move4 = 0
                
                current_cell = pygame.math.Vector2(self.center).distance_to(cell_center)
                move1 = pygame.math.Vector2(self.cell_picker.bottomleft).distance_to(cell_center)
                move2 = pygame.math.Vector2(self.cell_picker.bottomright).distance_to(cell_center)
                move3 = pygame.math.Vector2(self.cell_picker.topleft).distance_to(cell_center)
                move4 = pygame.math.Vector2(self.cell_picker.topright).distance_to(cell_center) 
                
                if move1 <= 10 or move2 <= 20 or current_cell <= 75:
                    self.move_list.append(cell)
                if self.is_king:
                    if move3 <= 10 or move4 <= 20 or current_cell <= 75:
                        self.move_list.append(cell)
        pprint.pprint(self.move_list)
        
    #def find_nearest_token(self, token):
        