import pygame

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