from typing import List
from enum import Enum

class Move:
    def __init__(self, origin: Square, dest: Square, capture:Piece=None):
        if capture is None:
            self.captures = []  # type: List[Piece]
        else:
            self.captures = [capture]

        self.origin = origin
        self.steps = [dest]

    def add_step(self, new_dest: Square, capture: Piece):
        self.steps.append(new_dest)
        self.captures.append(capture)

class PieceType(Enum):
    Black = 0
    White = 1


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
    def __init__(self, current_square, type, is_king=False):
        self.current_square = current_square
        self.type = type
        self.is_king = is_king

    @property
    def x(self):
        return self.current_square.x

    @property
    def y(self):
        return self.current_square.y

    def __str__(self):
        if self.type == PieceType.Black:
            return "X"
        else:
            return "O"

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

    def add_piece(self, square, type):
        piece = Piece(square, type)

        square.set_piece(piece)

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

                    self.add_piece(self.squares[y][x], piece_type)

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

    def get_piece_moves(self, piece: Piece) -> List[Move]:
        moves = []

        def add_close_moves(trying_x: int, trying_y: int):
            trying_square = self.get_square_by_coords(trying_x, trying_y)
            if trying_square is not None and trying_square.piece is None:
                moves.append(Move(piece.current_square, self.get_square_by_coords(trying_x, trying_y)))

        def get_jump_moves(trying_x: int, trying_y: int, direction_x: int, direction_y: int, colour: PieceType):
            jump_moves = []  # type: List[Move]
            over_square = self.get_square_by_coords(trying_x + 2*direction_x, trying_y + 2*direction_y)
            op_square = self.get_square_by_coords(trying_x + direction_x, trying_y + direction_y)

            if over_square is not None and op_square.piece is not None and op_square.piece.type != colour:
                jump_moves = get_jump_moves(trying_x + 2*direction_x,
                                            trying_y + 2*direction_y,
                                            direction_x,
                                            direction_y, colour)
                if len(jump_moves) == 0:
                    return [Move(piece.current_square, over_square)]
                else:
                    # NOTE: this method could be optimised
                    return [move.add_step(over_square, op_square.piece) for move in jump_moves]

            return jump_moves

        def add_jump_moves(trying_x, trying_y, direction_x, direction_y, colour):
            jump_moves = get_jump_moves(trying_x, trying_y, direction_x, direction_y, colour)
            moves.extend(jump_moves)

        if piece.is_king or piece.type == PieceType.White:
            add_close_moves(piece.x + 1, piece.y + 1)
            add_close_moves(piece.x - 1, piece.y + 1)

            add_jump_moves(piece.x, piece.y, 1, 1, piece.type)
            add_jump_moves(piece.x, piece.y, -1, 1, piece.type)

        if piece.is_king or piece.type == PieceType.Black:
            add_close_moves(piece.x - 1, piece.y - 1)
            add_close_moves(piece.x + 1, piece.y - 1)

            add_jump_moves(piece.x, piece.y, -1, -1, piece.type)
            add_jump_moves(piece.x, piece.y, 1, -1, piece.type)

        return moves

