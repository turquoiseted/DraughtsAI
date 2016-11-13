import unittest
from unittest import TestCase
from game_engine import Board, PieceType
from helper_funcs import get_checker_pattern


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
        # test simple moves
        piece = self.board.add_piece(self.board.squares[0][1], PieceType.White)
        self.assertSetEqual(
            set([move.steps[0] for move in self.board.get_piece_moves(piece)]),
            {
                self.board.squares[1][2],
                self.board.squares[1][0],
            }
        )

        # test jumping moves
        op_piece = self.board.add_piece(self.board.squares[1][2], PieceType.Black)
        self.assertSetEqual(
            set([move.steps[0] for move in self.board.get_piece_moves(piece)]),
            {
                self.board.squares[2][3],
                self.board.squares[1][0]
            }
        )

class TestHelperFuncs(TestCase):
    def test_get_checker_pattern(self):
        # Fixed testcase to be true by Thomas Hickman at 13/11/2016 15:38
        self.assertSequenceEqual(
            list(get_checker_pattern(2, 1, 3, 3)),
            [(1, 2), (1, 4), (2, 0), (2, 2), (3, 1), (3, 3)]
        )


if __name__ == "__main__":
    unittest.main()
