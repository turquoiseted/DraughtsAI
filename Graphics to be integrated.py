from tkinter import *
from tkinter import ttk

white = "O"
black = "X"
piece_selected = []
space_selected = []

lastx, lasty = 0, 0
def checker_board(x, y):
    if (x % 2  == 0):
        if (y % 2 != 0):
            return True
        else:
            return False
    else:
        if (y % 2 == 0):
            return True
        else:
            return False

def display_win_screen(winner):
    canvas.delete()
    create_board()
    set_board(sample_board)
    canvas.create_rectangle((90, 130, 700, 330), fill = "aquamarine", outline = "black", width = 10)
    
    
    if (winner == white):
        pass

    elif (winner == black):
        pass

    else:
        pass
        
def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

def key(event):
    print ("pressed", repr(event.char))

def coords_to_square(x, y):
    new_x = x*40 + 10
    new_y = y*40 + 10
    return [new_x, new_y]

def callback(event):
        global piece_selected
        global space_selected
        if (event.x < 410) and (event.y < 410):
            if (event.x > 10) and (event.y > 10):
                # Calculate the position from top left corner
                sub_x = (event.x - 10) % 40
                sub_y = (event.y - 10) % 40
                # Get the top left corner
                new_x = event.x - sub_x
                new_y = event.y - sub_y
                # Calculate the grid co-ordinates
                test_x = int((new_x - 10)/40)
                test_y = int((new_y - 10)/40)

                ####
                if (checker_board(test_x, test_y)):
                    if (check_piece(test_x, test_y, sample_board, white)):
                        if (len(piece_selected) == 0):
                            recty = canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), outline = "magenta2", width = 3, tags = "Piece")
                            piece_selected.append("Yes")
                            
                            # Placeholder to aquire dest

                            possible_moves(dest)
                            possible_captures(captures)

                            
                        else:
                            # Empties the Piece squares so can click on new square 
                            canvas.delete("Piece")
                            piece_selected = []         
                            recty = canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), outline = "magenta2", width = 3, tags = "Piece")
                            piece_selected.append("Yes")


                    elif (check_piece(test_x, test_y, sample_board, black)):
                        if (len(piece_selected) == 0):
                            recty = canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), outline = "magenta2", width = 3, tags = "Piece")
                            piece_selected.append("Yes")

                            # Placeholder to aquire dest

                            possible_moves(dest)
                            possible_captures(captures)
                            
                        else:
                            # Empties the Piece squares so can click on new square 
                            canvas.delete("Piece")
                            piece_selected = []         
                            recty = canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), outline = "magenta2", width = 3, tags = "Piece")
                            piece_selected.append("Yes")

                    else:
                        if (check_empty(test_x, test_y, sample_board, white)):
                            if (len(space_selected) == 0):
                                canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), fill = "magenta2", tags = "Space")
                                space_selected.append("Yes")
                            else:
                                #Empties the Space squares so can click on new square 
                                canvas.delete("Space")
                                space_selected = []
                                
                                canvas.create_rectangle((new_x, new_y, new_x + 40, new_y + 40), fill = "magenta2", tags = "Space")
                                space_selected.append("Yes")
                                  
                        

                            

def possible_moves(possible_moves):
    for moves in possible_moves:
        new_coords = coords_to_square(moves[0], moves[1])
        x = new_coords[0]
        y = new_coords[1]
        canvas.create_rectangle((x, y, x  + 40, y + 40), fill = "green")

def possible_captures(possible_captures):
    for captures in possible_captures:
        new_coords = coords_to_square(captures[0], captures[1])
        x = new_coords[0]
        y = new_coords[1]
        canvas.create_rectangle((x, y, x  + 40, y + 40), width = 3, outline = "red")

        
            
            

def check_piece(x, y, board, active_player):
    if (board[y][x] == active_player):
        return True
    else:
        return False

def check_empty(x, y, board, active_player):
    if (board[y][x] == "."):
        return True
    else:
        return False



root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("Draughts")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 420))

move = StringVar()

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.config(background = "AntiqueWhite2")
## canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
# canvas.pack()



def create_board():
    canvas.create_text((600, 50), text = "Draughts", font = ("Edwardian Script ITC", 60))
    canvas.create_text((520, 170), text = "Player 1 Taken Pieces", font = ("Times new roman", 16))
    canvas.create_text((520, 260), text = "Player 2 Taken Pieces", font = ("Times new roman", 16))
    canvas.create_text((580, 125), width = 320, text = "To play click on the piece you want to move and the space you want to move it to", font = ("Times new roman", 10))
    canvas.create_rectangle((10, 10, 410, 410), fill = "MistyRose2")

    # Even Rows & Columns
    start_x = 50
    start_y = 10
    end_x = 90
    end_y = 50
    
    for x in range(5):
        for y in range(5):
            canvas.create_rectangle((start_x + x*80, start_y + y*80, end_x + x*80, end_y + y*80), fill = "Hotpink4")

    # Odd Rows & Columns
    start_x = 10
    start_y = 50
    end_x = 50
    end_y = 90
    
    for x in range(5):
        for y in range(5):
            canvas.create_rectangle((start_x + x*80, start_y + y*80, end_x + x*80, end_y + y*80), fill = "Hotpink4")


    #Border
    canvas.create_line(10, 10, 410, 10, fill='black', width=1)
    canvas.create_line(10, 10, 10, 410, fill='black', width=1)
    canvas.create_line(410, 10, 410, 410, fill='black', width=1)
    canvas.create_line(10, 410, 410, 410, fill='black', width=1)


def set_board(board):
    start_x = 15
    start_y = 15
    
    end_x = 45
    end_y = 45

    total_white = 0
    total_black = 0
    
    for y in range(10):
        for x in range(10):
            if board[y][x] != ".":
                if board[y][x] == "O":
                    canvas.create_oval((start_x + x*40, start_y + y*40, end_x + x*40, end_y + y*40), fill = "white")
                    total_white += 1
                else:
                    canvas.create_oval((start_x + x*40, start_y + y*40, end_x + x*40, end_y + y*40), fill = "black", outline = "mistyrose3")
                    total_black += 1

    if total_white < 20:
        total_white = 20 - total_white
        for pieces in range(total_white):
            canvas.create_oval((430 + 15*pieces, 190, 460 + 15*pieces, 220), fill = "white")
    if total_black < 20:
        total_black = 20 - total_black
        for pieces in range(total_black):
            canvas.create_oval((430 + 15*pieces, 280, 460 + 15*pieces, 310), fill = "black", outline = "white")
            
            

    
    
# TESTS

sample_board = [[".", "O", ".", "O", ".", "O", ".", "O", ".", "O"],["O", ".", "O", ".", "O", ".", "O", ".", "O", "."],
                [".", "O", ".", "O", ".", "O", ".", ".", ".", "O"],["O", ".", "O", ".", "O", ".", "O", ".", "O", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],[".", ".", ".", ".", ".", ".", "O", ".", ".", "."],
                [".", "X", ".", "X", ".", "X", ".", "X", ".", "X"],["X", ".", "X", ".", "X", ".", "X", ".", "X", "."],
                [".", "X", ".", "X", ".", "X", ".", "X", ".", "X"],["X", ".", "X", ".", "X", ".", "X", ".", "X", "."]]

dest = [[1, 4], [3, 4]]
captures = [[6,5]]

create_board()
set_board(sample_board)
# display_win_screen(white)


root.mainloop()
