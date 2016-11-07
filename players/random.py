from Player import Player
from game_engine import Board, Piece, Square, PieceType

class RandomPlayer(Player):
    def __init__(self, board, color):
        self._board = board
        self._color = color

    def make_move(self):
        for i in Board.pieces[self._color]:
            i.get_piece_moves()
        #choose a random available move and do it
        pass
