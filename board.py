from array import *
import pygame

NUM_ROWS, NUM_COLS = 8, 8
SQUARE_SIZE = 100
PIECE_SIZE = 80

# rgb
CREAM = (243, 228, 198)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# loading in chess piece pngs
b_bishop = pygame.image.load("pieces/b_bishop.png")
b_king = pygame.image.load("pieces/b_king.png")
b_knight = pygame.image.load("pieces/b_knight.png")
b_pawn = pygame.image.load("pieces/b_pawn.png")
b_queen = pygame.image.load("pieces/b_queen.png")
b_rook = pygame.image.load("pieces/b_rook.png")
w_bishop = pygame.image.load("pieces/w_bishop.png")
w_king = pygame.image.load("pieces/w_king.png")
w_knight = pygame.image.load("pieces/w_knight.png")
w_pawn = pygame.image.load("pieces/w_pawn.png")
w_queen = pygame.image.load("pieces/w_queen.png")
w_rook = pygame.image.load("pieces/w_rook.png")

# piece array
pieces = [
    0,
    w_pawn,
    w_rook,
    w_knight,
    w_bishop,
    w_king,
    w_queen,
    b_queen,
    b_king,
    b_bishop,
    b_knight,
    b_rook,
    b_pawn,
]


class Board:
    def __init__(self):
        self.board = [
            [2, 3, 4, 5, 6, 4, 3, 2],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 5, 6, 4, 3, 2],
        ]
        self.selected_piece = None
        self.black_pieces = 16
        self.white_pieces = 16

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(NUM_ROWS):
            for col in range(row % 2, NUM_COLS, 2):
                pygame.draw.rect(
                    window,
                    CREAM,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def draw_pieces(self, window):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if self.board[row][col] == 0:
                    continue
                # draw all pieces
                if row < 4:
                    piece = pygame.transform.smoothscale(
                        pieces[-1 * self.board[row][col]], (PIECE_SIZE, PIECE_SIZE)
                    )
                else:
                    piece = pygame.transform.smoothscale(
                        pieces[self.board[row][col]], (PIECE_SIZE, PIECE_SIZE)
                    )
                window.blit(
                    piece,
                    (
                        col * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) / 2,
                        row * SQUARE_SIZE + (SQUARE_SIZE - PIECE_SIZE) / 2,
                    ),
                )
