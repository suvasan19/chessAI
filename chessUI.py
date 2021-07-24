# imports
from array import *

# import pygame library
import pygame

# Import pygame.locals for easier access to key coordinates
# from pygame.locals import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

NUM_ROWS, NUM_COLS = 8, 8
SQUARE_SIZE = 100

# rgb
CREAM = (243,228,198)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.black_pieces = 16
        self.white_pieces = 16

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(NUM_ROWS):
            for col in range(row % 2, NUM_COLS, 2):
                pygame.draw.rect(window, CREAM, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# loading in chess piece pngs
b_bishop = pygame.image.load("pieces/b_bishop.png")
b_bishop.set_colorkey((255, 255, 255), RLEACCEL)
b_king = pygame.image.load("pieces/b_king.png")
b_king.set_colorkey((255, 255, 255), RLEACCEL)
b_knight = pygame.image.load("pieces/b_knight.png")
b_knight.set_colorkey((255, 255, 255), RLEACCEL)
b_pawn = pygame.image.load("pieces/b_pawn.png")
b_pawn.set_colorkey((255, 255, 255), RLEACCEL)
b_queen = pygame.image.load("pieces/b_queen.png")
b_queen.set_colorkey((255, 255, 255), RLEACCEL)
b_rook = pygame.image.load("pieces/b_rook.png")
b_rook.set_colorkey((255, 255, 255), RLEACCEL)
w_bishop = pygame.image.load("pieces/w_bishop.png")
w_bishop.set_colorkey((255, 255, 255), RLEACCEL)
w_king = pygame.image.load("pieces/w_king.png")
w_king.set_colorkey((255, 255, 255), RLEACCEL)
w_knight = pygame.image.load("pieces/w_knight.png")
w_knight.set_colorkey((255, 255, 255), RLEACCEL)
w_pawn = pygame.image.load("pieces/w_pawn.png")
w_pawn.set_colorkey((255, 255, 255), RLEACCEL)
w_queen = pygame.image.load("pieces/w_queen.png")
w_queen.set_colorkey((255, 255, 255), RLEACCEL)
w_rook = pygame.image.load("pieces/w_rook.png")
w_rook.set_colorkey((255, 255, 255), RLEACCEL)


# init pygame library
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 800]) #was 550 500
# caption of window
pygame.display.set_caption('Chess')

# initial chess board
#board = [
#    [2, 3, 4, 5, 6, 4, 3, 2],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [2, 3, 4, 5, 6, 4, 3, 2],
#]


# infinite loop for pygame
running = True
while running:
    board = Board()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    board.draw_squares(screen)
    # update display or something? idk wht this line does
    pygame.display.flip()

''' 
    # draw 64 squares
    for i in range(0, 8):
        for j in range(0, 8):
            if (i % 2 == 1 and j % 2 == 1) or (i % 2 == 0 and j % 2 == 0):
                color = (249, 172, 113)
            if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                color = (103, 51, 20)
            pygame.draw.rect(
                screen, color, pygame.Rect(25 + 50 * (j + 1), 50 * (i + 1), 50, 50)
            )

            # drawing pieces
            if board[i][j] == 2:
                if i < 4:
                    rook = pygame.transform.smoothscale(b_rook, (40, 40))
                elif i > 4:
                    rook = pygame.transform.smoothscale(w_rook, (40, 40))
                piece = rook.get_rect(center=(50 + 50 * (j + 1), 25 + 50 * (i + 1)))
                screen.blit(rook, piece)
'''


# quit the program
pygame.quit()