from tkinter import *
from helper_funcs import get_checker_pattern

class DraughtsUI:
    def __init__(self):
        self.root = Tk()
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.title("Draughts")
        self.root.resizable(width=False, height=False)
        self.root.geometry('{}x{}'.format(800, 420))
        move = StringVar()

        self.canvas = Canvas(self.root)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S))
        self.canvas.config(background ="lemon chiffon")


        move = Entry(self.root, width = 30)
        #move.place(x=10, y=10, width=100)
        move.grid(row = 0, column = 0, sticky = (S, E), pady = 60, padx = 60)

        self.create_board()
        self.root.mainloop()

    def draw_board(self):
        def create_rect_at_pos(row, col, fill):
            self.canvas.create_rectangle((row * 40 + 10, col * 40 + 10, row * 40 + 50, col * 40 + 50), fill=fill)

        for (row, col) in get_checker_pattern(init_offset=0, init_row=0, rows=10, max_col=10):
            create_rect_at_pos(row, col, "brown")

        for (row, col) in get_checker_pattern(init_offset=1, init_row=0, rows=10, max_col=10):
            create_rect_at_pos(row, col, "orange")

    def create_board(self):
        self.canvas.create_text((600, 50), text ="Draughts", font = ("Edwardian Script ITC", 60))
        self.canvas.create_text((520, 150), text ="Player 1 Taken Pieces", font = ("Times new roman", 16))
        self.canvas.create_text((520, 250), text ="Player 2 Taken Pieces", font = ("Times new roman", 16))
        self.canvas.create_text((480, 350), text ="Enter Move", font = ("Times new roman", 16))
        self.canvas.create_rectangle((10, 10, 410, 410), fill ="lightgoldenrod")

        self.draw_board()

    def set_pieces_black(self):
        #Row 4
        self.canvas.create_oval((55, 375, 85, 405), fill ="black")
        self.canvas.create_oval((135, 375, 165, 405), fill ="black")
        self.canvas.create_oval((215, 375, 245, 405), fill ="black")
        self.canvas.create_oval((295, 375, 325, 405), fill ="black")
        self.canvas.create_oval((375, 375, 405, 405), fill ="black")

        #Row 3
        self.canvas.create_oval((15, 335, 45, 365), fill ="black")
        self.canvas.create_oval((95, 335, 125, 365), fill ="black")
        self.canvas.create_oval((175, 335, 205, 365), fill ="black")
        self.canvas.create_oval((255, 335, 285, 365), fill ="black")
        self.canvas.create_oval((335, 335, 365, 365), fill ="black")

        #Row 2
        self.canvas.create_oval((55, 295, 85, 325), fill ="black")
        self.canvas.create_oval((135, 295, 165, 325), fill ="black")
        self.canvas.create_oval((215, 295, 245, 325), fill ="black")
        self.canvas.create_oval((295, 295, 325, 325), fill ="black")
        self.canvas.create_oval((375, 295, 405, 325), fill ="black")

        #Row 1
        self.canvas.create_oval((15, 255, 45, 285), fill ="black")
        self.canvas.create_oval((95, 255, 125, 285), fill ="black")
        self.canvas.create_oval((175, 255, 205, 285), fill ="black")
        self.canvas.create_oval((255, 255, 285, 285), fill ="black")
        self.canvas.create_oval((335, 255, 365, 285), fill ="black")

    def set_pieces_white(self):
        #Row 1
        self.canvas.create_oval((55, 135, 85, 165), fill ="white")
        self.canvas.create_oval((135, 135, 165, 165), fill ="white")
        self.canvas.create_oval((215, 135, 245, 165), fill ="white")
        self.canvas.create_oval((295, 135, 325, 165), fill ="white")
        self.canvas.create_oval((375, 135, 405, 165), fill ="white")

        #Row 2
        self.canvas.create_oval((15, 95, 45, 125), fill ="white")
        self.canvas.create_oval((95, 95, 125, 125), fill ="white")
        self.canvas.create_oval((175, 95, 205, 125), fill ="white")
        self.canvas.create_oval((255, 95, 285, 125), fill ="white")
        self.canvas.create_oval((335, 95, 365, 125), fill ="white")

        #Row 3
        self.canvas.create_oval((55, 55, 85, 85), fill ="white")
        self.canvas.create_oval((135, 55, 165, 85), fill ="white")
        self.canvas.create_oval((215, 55, 245, 85), fill ="white")
        self.canvas.create_oval((295, 55, 325, 85), fill ="white")
        self.canvas.create_oval((375, 55, 405, 85), fill ="white")

        #Row 4
        self.canvas.create_oval((15, 15, 45, 45), fill ="white")
        self.canvas.create_oval((95, 15, 125, 45), fill ="white")
        self.canvas.create_oval((175, 15, 205, 45), fill ="white")
        self.canvas.create_oval((255, 15, 285, 45), fill ="white")
        self.canvas.create_oval((335, 15, 365, 45), fill ="white")

if __name__ == "__main__":
    DraughtsUI()