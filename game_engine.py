class Board:
    def __init__(self):
        self.squares = []
        self.pieces = {
            PieceType.Black: [],
            PieceType.White: []
        }

        for row in range(10):
            row = []

            for column in range(10):
                row.append(Square(column, row))

            self.squares.append(row)

    def add_piece(self, x, y, type):
        piece = Piece(x, y, type)

        self.squares[y][x].set_piece(piece)

        self.pieces[type].append(piece)

    def remove_piece(self, x, y):
        piece = self.squares[y][x]
        self.squares[y][x].set_piece(None)

        self.pieces[piece.type].remove(piece)

    def init_default_state(self):
        def fill_squares(init_offset, init_row, piece_type):
            offset = init_offset
            for piece_y in range(4):
                for piece_x in range(5):
                    y = piece_y + init_row
                    x = piece_x * 2 + offset

                    self.add_piece(x, y, piece_type)

                if offset == 0:
                    offset = 1
                else:
                    offset = 0
        fill_squares(1, 0, PieceType.White)
        fill_squares(1, 6, PieceType.Black)

    def __str__(self):
        lines = []

        for row in self.squares:
            line = ""
            for square in row:
                line += str(square)

            lines.append(line)

        return "\n".join(lines)

    def get_square_by_coords(self, x, y):
        if y < 0 or x < 0 or y >= len(self.squares) or x >= len(self.squares[0]) :
            return None
        else:
            return self.squares[y][x]

    def get_piece_moves(self, piece):
        moves = []

        def add_close_moves(trying_x, trying_y):
            trying_square = self.get_square_by_coords(trying_x, trying_y)
            if trying_square is not None and trying_square.piece is None:
                moves.append(self.get_square_by_coords(trying_x, trying_y))

        def add_jump_moves(op_x, op_y, over_x, over_y, mycol):
            over_square = self.get_square_by_coords(over_x, over_y)
            op_square = self.get_square_by_coords(op_x, op_y)
            if over_square is not None and op_square.piece is not None and op_square.piece.type != mycol:
                moves.append(self.get_square_by_coords(over_x, over_y))

        if piece.is_king or piece.type == PieceType.White:
            add_close_moves(piece.x + 1, piece.y + 1)
            add_close_moves(piece.x - 1, piece.y + 1)

        if piece.is_king or piece.type == PieceType.Black:
            add_close_moves(piece.x - 1, piece.y - 1)
            add_close_moves(piece.x + 1, piece.y - 1)

        if piece.is_king or piece.type == PieceType.White:
            add_jump_moves(piece.x + 1, piece.y + 1, piece.x + 2, piece.y + 2, piece.type)
            add_jump_moves(piece.x - 1, piece.y + 1, piece.x - 2, piece.y + 2, piece.type)

        if piece.is_king or piece.type == PieceType.Black:
            add_jump_moves(piece.x - 1, piece.y - 1, piece.x - 2, piece.y - 2, piece.type)
            add_jump_moves(piece.x + 1, piece.y - 1, piece.x + 2, piece.y - 2, piece.type)

        return moves

class PieceType:
    Black = "black"
    White = "white"

class Square:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def set_piece(self, piece):
        self.piece = piece

    def __str__(self):
        if self.piece is None:
            return "."
        else:
            return str(self.piece)


class Piece:
    def __init__(self, x, y, type, is_king = False):
        self.x = x
        self.y = y
        self.type = type
        self.is_king = is_king

    def __str__(self):
        if self.type == PieceType.Black:
            return "X"
        else:
            return "O"


