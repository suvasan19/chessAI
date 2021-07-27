class Piece:
    def __init__(self, color):
        self.color = color


class Pawn(Piece):
    def __init__(self):
        self.move_two = False


class Rook(Piece):
    def __init__(self):
        self.moved = False


class King(Piece):
    def __init__(self):
        self.moved = False
        self.check = False


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass
