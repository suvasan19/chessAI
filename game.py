from piece import *

def findMoves(board, x, y, player):
    # player = true (black)
    if player == True:
        one = 1
    # white
    else:
        one = -1

    moves = {}
    """
    Returns the 
    """

    piece = board[x][y]
    first = False

    # Pawn = 1
    if isinstance(piece, Pawn):
        if (piece.color=="white" and x == 1) or (piece.color == "black" and x == 6):
            first = True

        # if first move for pawn, returns 1 and 2 moves
        if first:
            moves.append((x, y + one), (x, y + one + one))

        # Moves forward 1 if not blocked
        if board[x][y + one] == 0:
            moves.append((x, y + one))

        # Check if diagonal has an opposite piece
        if board[x + one][y + one].color != piece.color:
            moves.append((x + one, y + one))
        if board[x + one][y - one].color != piece.color:
            moves.append((x + one, y - one))

        return moves

    # Rook = 2
    if isinstance(piece,Rook):
        index = 1
        # if not blocked, can move forward
        while (y + index < 8) and (board[x][y + index] == 0):
            moves.append((x, y + index))
            index += 1
        index = 1
        # if not blocked, can move backwards
        while (y - index >= 0) and (board[x][y - index] == 0):
            moves.append((x, y - index))
            index += 1
        index = 1
        # if not blocked, can move right
        while (x + index < 8) and (board[x + index][y] == 0):
            moves.append((x + index, y))
            index += 1
        index = 1
        # if not blocked, can move left
        while (x - index >= 0) and (board[x - index][y] == 0):
            moves.append((x - index, y))
            index += 1

        return moves

    # #Knight = 3
    # if(board[x][y] == 3):

    #     #need to figure out how to get color of piece.
    #     if(board[x+2][y+3] )

    #     if(board[x+3][y+2])