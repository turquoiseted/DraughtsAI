class SquareType:
    Empty = "none"
    Black = "black"
    White = "white"

class Square:
    def __init__(self, _type=SquareType.Empty):
        self.type = _type

    def __str__(self):
        if self.type == SquareType.Empty:
            return "."
        elif self.type == SquareType.Black:
            return "X"
        else:
            return "O"