# imports
from array import *
from board import Board
from game import *

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
CREAM = (243, 228, 198)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# init pygame library
pygame.init()

# set up the drawing window
screen = pygame.display.set_mode([800, 800])  # was 550 500
# caption of window
pygame.display.set_caption("Chess")

# initial chess board
# board = [
#    [2, 3, 4, 5, 6, 4, 3, 2],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0, 0, 0],
#    [1, 1, 1, 1, 1, 1, 1, 1],
#    [2, 3, 4, 5, 6, 4, 3, 2],
# ]

# are any squares highlighted?
clicked = False
x = 0
y = 0

# infinite loop for pygame
running = True
while running:
    board = Board()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # did user click on screen?
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # get x, y coords of mouse click
            x, y = pygame.mouse.get_pos()
            # standardize x, y to be coords in 8x8 array
            x = int(x / 100)
            y = int(y / 100)
            clicked = True

    board.draw_squares(screen)

    # if mouse is clicked, highlight piece and its moves
    if clicked == True:
        # highlight the square
        highlight = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))  # the size of your rect
        highlight.set_alpha(128)  # alpha level
        highlight.fill((186, 208, 107))  # this fills the entire surface
        screen.blit(highlight, (x * SQUARE_SIZE, y * SQUARE_SIZE))

        # figure out which piece it is

    # draw pieces on board
    board.draw_pieces(screen)

    # update display or something? idk wht this line does
    pygame.display.flip()

""" 
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
"""


# quit the program
pygame.quit()