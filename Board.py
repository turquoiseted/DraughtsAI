from Square import Square
from Square import SquareType

class Board:
    def __init__(self):
        self._squares = []
        for row in range(10):
            row = []

            for column in range(10):
                row.append(Square())

            self._squares.append(row)

    def init_default_state(self):
        def fill_squares(init_offset, init_row, square_type):
            offset = init_offset
            for row in range(4):
                for x in range(5):
                    self._squares[row + init_row][x * 2 + offset].type = square_type

                if offset == 0:
                    offset = 1
                else:
                    offset = 0
        fill_squares(0, 0, SquareType.White)
        fill_squares(1, 6, SquareType.Black)

    def __str__(self):
        lines = []

        for row in self._squares:
            line = ""
            for square in row:
                line += str(square)

            lines.append(line)

        return "\n".join(lines)

