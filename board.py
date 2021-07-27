from array import *
from piece import *
import pygame

NUM_ROWS, NUM_COLS = 8, 8
SQUARE_SIZE = 100
PIECE_SIZE = 80

# rgb
CREAM = (243, 228, 198)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# loading in chess piece pngs
b_bishop1 = Bishop("black")
b_bishop2 = Bishop("black")
b_king1 = King("black")
b_knight1 = Knight("black")
b_knight2 = Knight("black")
b_pawn1 = Pawn("black")
b_pawn2 = Pawn("black")
b_pawn3 = Pawn("black")
b_pawn4 = Pawn("black")
b_pawn5 = Pawn("black")
b_pawn6 = Pawn("black")
b_pawn7 = Pawn("black")
b_pawn8 = Pawn("black")
b_queen1 = Queen("black")
b_rook1 = Rook("black")
b_rook2 = Rook("black")

w_bishop1 = Bishop("white")
w_bishop2 = Bishop("white")
w_king1 = King("white")
w_knight1 = Knight("white")
w_knight2 = Knight("white")
w_pawn1 = Pawn("white")
w_pawn2 = Pawn("white")
w_pawn3 = Pawn("white")
w_pawn4 = Pawn("white")
w_pawn5 = Pawn("white")
w_pawn6 = Pawn("white")
w_pawn7 = Pawn("white")
w_pawn8 = Pawn("white")
w_queen1 = Queen("white")
w_rook1 = Rook("white")
w_rook2 = Rook("white")

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
            [b_rook1, b_knight1, b_bishop1, b_queen1, b_king1, b_bishop2, b_knight2, b_rook2],
            [b_pawn1, b_pawn2, b_pawn3, b_pawn4, b_pawn5, b_pawn6, b_pawn7, b_pawn8],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [w_pawn1, w_pawn2, w_pawn3, w_pawn4, w_pawn5, w_pawn6, w_pawn7, w_pawn8],
            [w_rook1, w_knight1, w_bishop1, w_queen1, w_king1, w_bishop2, w_knight2, w_rook2]
        ]

        self.turn = "white"
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
