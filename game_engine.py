class Board:
    def __init__(self):
        self.squares = []
        for row in range(10):
            row = []

            for column in range(10):
                row.append(Square())

            self.squares.append(row)

    def init_default_state(self):
        def fill_squares(init_offset, init_row, piece_type):
            offset = init_offset
            for piece_y in range(4):
                for piece_x in range(5):
                    y = piece_y + init_row
                    x = piece_x * 2 + offset

                    self.squares[y][x] = Square(Piece(x, y, piece_type))

                if offset == 0:
                    offset = 1
                else:
                    offset = 0
        fill_squares(0, 0, PieceType.White)
        fill_squares(1, 6, PieceType.Black)

    def __str__(self):
        lines = []

        for row in self.squares:
            line = ""
            for square in row:
                line += str(square)

            lines.append(line)

        return "\n".join(lines)

class PieceType:
    Black = "black"
    White = "white"

class Square:
    def __init__(self, piece = None):
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return "."
        else:
            return str(self.piece)


class Piece:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        if self.type == PieceType.Black:
            return "X"
        else:
            return "O"