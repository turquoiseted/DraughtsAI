import unittest
from unittest import TestCase
from game_engine import Board, PieceType

class TestBoard(TestCase):
    def setUp(self):
        self.board = Board()

    def test_setup_initial_state(self):
        self.board.init_default_state()
        correct_output = "O.O.O.O.O.\n"\
                         ".O.O.O.O.O\n"\
                         "O.O.O.O.O.\n"\
                         ".O.O.O.O.O\n"\
                         "..........\n"\
                         "..........\n"\
                         ".X.X.X.X.X\n"\
                         "X.X.X.X.X.\n"\
                         ".X.X.X.X.X\n"\
                         "X.X.X.X.X."

        self.assertEqual(self.board.get_str_form(), correct_output)

    def test_get_piece_moves(self):
        piece = self.board.add_piece(self.board.squares[0][1], PieceType.White)
        self.assertSequenceEqual(
            [move.steps[0] for move in self.board.get_piece_moves(piece)],
            [
                self.board.squares[1][2],
                self.board.squares[1][0],
            ]
        )


if __name__ == "__main__":
    unittest.main()
