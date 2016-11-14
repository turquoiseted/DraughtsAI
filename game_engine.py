from typing import List, Union
from enum import Enum

from helper_funcs import get_checker_pattern


class PieceType(Enum):
    Black = 0
    White = 1


class DefaultRepr:
    def __repr__(self):
        return "{}({})".format(self.__class__, self.__dict__)


class Square(DefaultRepr):
    def __init__(self, x: int, y: int, piece: 'Piece' = None):
        self.x = x
        self.y = y
        self.piece = piece

    def set_piece(self, piece):
        self.piece = piece

    def get_char_form(self):
        if self.piece is None:
            return "."
        else:
            return str(self.piece)

    def __str__(self):
        return "Square ({}, {})".format(self.x, self.y)


class Piece(DefaultRepr):
    def __init__(self, current_square: Square, type: PieceType, is_king=False):
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


class Move:
    def __init__(self, origin: Piece, steps: Union[Square, List[Square]], captures: Union[Piece, List[Piece]] = None):
        if captures is None:
            self.captures = []  # type: List[Piece]
        elif isinstance(captures, list):
            self.captures = captures
        else:
            self.captures = [captures]

        self.origin = origin

        if isinstance(steps, list):
            self.steps = steps
        else:
            self.steps = [steps]

    def clone(self):
        return Move(self.origin, self.steps, self.captures)

    def add_step(self, new_dest: Square, capture: Piece):
        self.steps.append(new_dest)
        self.captures.append(capture)

    @property
    def dest(self):
        return self.steps[-1]

    def __str__(self):
        return " -> ".join([str(sq) for sq in [self.origin] + self.steps])


class Board(DefaultRepr):
    def __init__(self):
        self.squares = []
        self.piece_by_type = {
            PieceType.Black: [],
            PieceType.White: []
        }

        for row_num in range(10):
            row = []

            for column_num in range(10):
                row.append(Square(column_num, row_num))

            self.squares.append(row)

    @property
    def all_pieces(self):
        return self.piece_by_type[PieceType.Black] + self.piece_by_type[PieceType.White]

    def add_piece(self, square, type, is_king=False):
        piece = Piece(square, type, is_king)

        square.set_piece(piece)

        self.piece_by_type[type].append(piece)

        return piece

    def remove_piece(self, x, y):
        piece = self.squares[y][x]
        self.squares[y][x].set_piece(None)

        self.piece_by_type[piece.type].remove(piece)

        return piece

    def init_default_state(self):
        def fill_squares(init_offset, init_row, piece_type):
            for (col, row) in get_checker_pattern(init_offset, init_row, 4, 10):
                self.add_piece(self.squares[col][row], piece_type)

        fill_squares(0, 0, PieceType.White)
        fill_squares(0, 6, PieceType.Black)

    def get_str_form(self):
        lines = []

        for row in self.squares:
            line = ""
            for square in row:
                line += square.get_char_form()

            lines.append(line)

        return "\n".join(lines)

    def get_square_by_coords(self, x, y) -> Square:
        if y < 0 or x < 0 or y >= len(self.squares) or x >= len(self.squares[0]):
            return None
        else:
            return self.squares[y][x]

    def apply_move(self, move: Move):
        move.origin.current_square.piece = None
        move.origin.current_square = move.dest
        move.dest.piece = move.origin

    def get_piece_moves(self, piece: Piece) -> List[Move]:
        moves = []

        def add_close_moves(trying_x: int, trying_y: int):
            trying_square = self.get_square_by_coords(trying_x, trying_y)
            if trying_square is not None and trying_square.piece is None:
                moves.append(Move(piece, self.get_square_by_coords(trying_x, trying_y)))

        def add_jump_moves(direction_x: int, direction_y: int):
            jump_moves = []  # type: List[Move]

            (current_x, current_y) = (piece.x, piece.y)

            over_square = self.get_square_by_coords(current_x + 2 * direction_x, current_y + 2 * direction_y)
            op_square = self.get_square_by_coords(current_x + direction_x, current_y + direction_y)

            print(over_square, op_square, repr(op_square.piece))
            while over_square is not None \
                    and op_square is not None \
                    and over_square.piece is None \
                    and op_square.piece is not None \
                    and op_square.piece.type != piece.type:
                if len(jump_moves) == 0:
                    jump_moves.append(Move(piece, over_square, op_square.piece))
                else:
                    move = jump_moves[-1].clone()
                    move.add_step(over_square, op_square.piece)
                    jump_moves.append(move)

                (current_x, current_y) = (over_square.x, over_square.y)

                over_square = self.get_square_by_coords(current_x + 2 * direction_x, current_y + 2 * direction_y)
                op_square = self.get_square_by_coords(current_x + direction_x, current_y + direction_y)

        if piece.is_king or piece.type == PieceType.White:
            add_close_moves(piece.x + 1, piece.y + 1)
            add_close_moves(piece.x - 1, piece.y + 1)

            add_jump_moves(1, 1)
            add_jump_moves(-1, 1)

        if piece.is_king or piece.type == PieceType.Black:
            add_close_moves(piece.x - 1, piece.y - 1)
            add_close_moves(piece.x + 1, piece.y - 1)

            add_jump_moves(-1, -1)
            add_jump_moves(1, -1)

        return moves
