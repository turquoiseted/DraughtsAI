from tkinter import *

from game_engine import Board, Piece, Move
from helper_funcs import get_checker_pattern


class DraughtsUI:
    def __init__(self):
        self._root = Tk()
        self._root.columnconfigure(0, weight=1)
        self._root.rowconfigure(0, weight=1)
        self._root.title("Draughts")
        self._root.resizable(width=False, height=False)
        self._root.geometry('{}x{}'.format(800, 420))

        self._canvas = Canvas(self._root)
        self._canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self._canvas.config(background="lemon chiffon")

        self._ovals = []

        moveTextBox = StringVar()
        moveTextBox = Entry(self._root, width=30)
        # moveTextBox.place(x=10, y=10, width=100)
        moveTextBox.grid(row=0, column=0, sticky=(S, E), pady=60, padx=60)

        moveButton = None  # TODO: add a button and receive input

        self._draw_main_ui()
        self.set_pieces_black()
        self._root.mainloop()

    def draw_move(self, move: Move):
        """
        Applies the specified move
        """
        pass

    def _on_text_move_entered(self):
        # parse in a board class/another class, apply as a move
        pass

    def _draw_board_background(self):
        def create_rect_at_pos(row, col, fill):
            self._canvas.create_rectangle((row * 40 + 10, col * 40 + 10, row * 40 + 50, col * 40 + 50), fill=fill)

        for (row, col) in get_checker_pattern(init_offset=0, init_row=0, rows=10, max_col=10):
            create_rect_at_pos(row, col, "brown")

        for (row, col) in get_checker_pattern(init_offset=1, init_row=0, rows=10, max_col=10):
            create_rect_at_pos(row, col, "orange")

    def _draw_main_ui(self):
        self._canvas.create_text((600, 50), text="Draughts", font=("Edwardian Script ITC", 60))
        self._canvas.create_text((520, 150), text="Player 1 Taken Pieces", font=("Times new roman", 16))
        self._canvas.create_text((520, 250), text="Player 2 Taken Pieces", font=("Times new roman", 16))
        self._canvas.create_text((480, 350), text="Enter Move", font=("Times new roman", 16))
        self._canvas.create_rectangle((10, 10, 410, 410), fill="lightgoldenrod")

        self._draw_board_background()

    def set_pieces_black(self):
        # Row 4
        self._canvas.create_oval((55, 375, 85, 405), fill="black")
        self._canvas.create_oval((135, 375, 165, 405), fill="black")
        self._canvas.create_oval((215, 375, 245, 405), fill="black")
        self._canvas.create_oval((295, 375, 325, 405), fill="black")
        self._canvas.create_oval((375, 375, 405, 405), fill="black")

        # Row 3
        self._canvas.create_oval((15, 335, 45, 365), fill="black")
        self._canvas.create_oval((95, 335, 125, 365), fill="black")
        self._canvas.create_oval((175, 335, 205, 365), fill="black")
        self._canvas.create_oval((255, 335, 285, 365), fill="black")
        self._canvas.create_oval((335, 335, 365, 365), fill="black")

        # Row 2
        self._canvas.create_oval((55, 295, 85, 325), fill="black")
        self._canvas.create_oval((135, 295, 165, 325), fill="black")
        self._canvas.create_oval((215, 295, 245, 325), fill="black")
        self._canvas.create_oval((295, 295, 325, 325), fill="black")
        self._canvas.create_oval((375, 295, 405, 325), fill="black")

        # Row 1
        self._canvas.create_oval((15, 255, 45, 285), fill="black")
        self._canvas.create_oval((95, 255, 125, 285), fill="black")
        self._canvas.create_oval((175, 255, 205, 285), fill="black")
        self._canvas.create_oval((255, 255, 285, 285), fill="black")
        self._canvas.create_oval((335, 255, 365, 285), fill="black")

    def set_pieces_white(self):
        # Row 1
        self._canvas.create_oval((55, 135, 85, 165), fill="white")
        self._canvas.create_oval((135, 135, 165, 165), fill="white")
        self._canvas.create_oval((215, 135, 245, 165), fill="white")
        self._canvas.create_oval((295, 135, 325, 165), fill="white")
        self._canvas.create_oval((375, 135, 405, 165), fill="white")

        # Row 2
        self._canvas.create_oval((15, 95, 45, 125), fill="white")
        self._canvas.create_oval((95, 95, 125, 125), fill="white")
        self._canvas.create_oval((175, 95, 205, 125), fill="white")
        self._canvas.create_oval((255, 95, 285, 125), fill="white")
        self._canvas.create_oval((335, 95, 365, 125), fill="white")

        # Row 3
        self._canvas.create_oval((55, 55, 85, 85), fill="white")
        self._canvas.create_oval((135, 55, 165, 85), fill="white")
        self._canvas.create_oval((215, 55, 245, 85), fill="white")
        self._canvas.create_oval((295, 55, 325, 85), fill="white")
        self._canvas.create_oval((375, 55, 405, 85), fill="white")

        # Row 4
        self._canvas.create_oval((15, 15, 45, 45), fill="white")
        self._canvas.create_oval((95, 15, 125, 45), fill="white")
        self._canvas.create_oval((175, 15, 205, 45), fill="white")
        self._canvas.create_oval((255, 15, 285, 45), fill="white")
        self._canvas.create_oval((335, 15, 365, 45), fill="white")


if __name__ == "__main__":
    DraughtsUI()
