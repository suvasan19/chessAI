class Piece:
    def __init__(self, color):
        self.color = color


class Pawn(Piece):
    def __init__(self, color, move_two=False):
        super().__init__(color)
        self.move_two = move_two


class Rook(Piece):
    def __init__(self, color , moved=False):
        super().__init__(color)
        self.moved = moved


class King(Piece):
    def __init__(self, color, moved=False, check=False):
        super().__init__(color)
        self.moved = moved
        self.check = check


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass