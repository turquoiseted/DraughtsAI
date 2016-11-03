from tkinter import *
from tkinter import ttk

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("Draughts")
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(800, 420))

move = StringVar()

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.config(background = "lemon chiffon")


move = Entry(root, width = 30)
#move.place(x=10, y=10, width=100) 
move.grid(row = 0, column = 0, sticky = (S, E), pady = 60, padx = 60)





def create_board():
    canvas.create_text((600, 50), text = "Draughts", font = ("Edwardian Script ITC", 60))
    canvas.create_text((520, 150), text = "Player 1 Taken Pieces", font = ("Times new roman", 16))
    canvas.create_text((520, 250), text = "Player 2 Taken Pieces", font = ("Times new roman", 16))
    canvas.create_text((480, 350), text = "Enter Move", font = ("Times new roman", 16))
    canvas.create_rectangle((10, 10, 410, 410), fill = "lightgoldenrod")

    
    
    
    # Rows 1&2
    canvas.create_rectangle((10, 10, 50, 50), fill = "brown")
    canvas.create_rectangle((90, 10, 130, 50), fill = "brown")
    canvas.create_rectangle((50, 50, 90, 90), fill = "brown")
    canvas.create_rectangle((130, 50, 170, 90), fill = "brown")
    canvas.create_rectangle((170, 10, 210, 50), fill = "brown")
    canvas.create_rectangle((210, 50, 250, 90), fill = "brown")
    canvas.create_rectangle((250, 10, 290, 50), fill = "brown")
    canvas.create_rectangle((290, 50, 330, 90), fill = "brown")
    canvas.create_rectangle((330, 10, 370, 50), fill = "brown")
    canvas.create_rectangle((370, 50, 410, 90), fill = "brown")

    # Rows 3&4
    canvas.create_rectangle((10, 90, 50, 130), fill = "brown")
    canvas.create_rectangle((90, 90, 130, 130), fill = "brown")
    canvas.create_rectangle((50, 130, 90, 170), fill = "brown")
    canvas.create_rectangle((130, 130, 170, 170), fill = "brown")
    canvas.create_rectangle((170, 90, 210, 130), fill = "brown")
    canvas.create_rectangle((210, 130, 250, 170), fill = "brown")
    canvas.create_rectangle((250, 90, 290, 130), fill = "brown")
    canvas.create_rectangle((290, 130, 330, 170), fill = "brown")
    canvas.create_rectangle((330, 90, 370, 130), fill = "brown")
    canvas.create_rectangle((370, 130, 410, 170), fill = "brown")

    # Rows 5&6
    canvas.create_rectangle((10, 170, 50, 210), fill = "brown")
    canvas.create_rectangle((90, 170, 130, 210), fill = "brown")
    canvas.create_rectangle((50, 210, 90, 250), fill = "brown")
    canvas.create_rectangle((130, 210, 170, 250), fill = "brown")
    canvas.create_rectangle((170, 170, 210, 210), fill = "brown")
    canvas.create_rectangle((210, 210, 250, 250), fill = "brown")
    canvas.create_rectangle((250, 170, 290, 210), fill = "brown")
    canvas.create_rectangle((290, 210, 330, 250), fill = "brown")
    canvas.create_rectangle((330, 170, 370, 210), fill = "brown")
    canvas.create_rectangle((370, 210, 410, 250), fill = "brown")

    # Row 7&8
    canvas.create_rectangle((10, 250, 50, 290), fill = "brown")
    canvas.create_rectangle((90, 250, 130, 290), fill = "brown")
    canvas.create_rectangle((50, 290, 90, 330), fill = "brown")
    canvas.create_rectangle((130, 290, 170, 330), fill = "brown")
    canvas.create_rectangle((170, 250, 210, 290), fill = "brown")
    canvas.create_rectangle((210, 290, 250, 330), fill = "brown")
    canvas.create_rectangle((250, 250, 290, 290), fill = "brown")
    canvas.create_rectangle((290, 290, 330, 330), fill = "brown")
    canvas.create_rectangle((330, 250, 370, 290), fill = "brown")
    canvas.create_rectangle((370, 290, 410, 330), fill = "brown")

    # Rows 9&10
    canvas.create_rectangle((10, 330, 50, 370), fill = "brown")
    canvas.create_rectangle((90, 330, 130, 370), fill = "brown")
    canvas.create_rectangle((50, 370, 90, 410), fill = "brown")
    canvas.create_rectangle((130, 370, 170, 410), fill = "brown")
    canvas.create_rectangle((170, 330, 210, 370), fill = "brown")
    canvas.create_rectangle((210, 370, 250, 410), fill = "brown")
    canvas.create_rectangle((250, 330, 290, 370), fill = "brown")
    canvas.create_rectangle((290, 370, 330, 410), fill = "brown")
    canvas.create_rectangle((330, 330, 370, 370), fill = "brown")
    canvas.create_rectangle((370, 370, 410, 410), fill = "brown")

    #Border
    canvas.create_line(10, 10, 410, 10, fill='black', width=1)
    canvas.create_line(10, 10, 10, 410, fill='black', width=1)
    canvas.create_line(410, 10, 410, 410, fill='black', width=1)
    canvas.create_line(10, 410, 410, 410, fill='black', width=1)

def set_pieces_black():
    #Row 4
    canvas.create_oval((55, 375, 85, 405), fill = "black")
    canvas.create_oval((135, 375, 165, 405), fill = "black")
    canvas.create_oval((215, 375, 245, 405), fill = "black")
    canvas.create_oval((295, 375, 325, 405), fill = "black")
    canvas.create_oval((375, 375, 405, 405), fill = "black")
    
    #Row 3
    canvas.create_oval((15, 335, 45, 365), fill = "black")
    canvas.create_oval((95, 335, 125, 365), fill = "black")
    canvas.create_oval((175, 335, 205, 365), fill = "black")
    canvas.create_oval((255, 335, 285, 365), fill = "black")
    canvas.create_oval((335, 335, 365, 365), fill = "black")

    #Row 2
    canvas.create_oval((55, 295, 85, 325), fill = "black")
    canvas.create_oval((135, 295, 165, 325), fill = "black")
    canvas.create_oval((215, 295, 245, 325), fill = "black")
    canvas.create_oval((295, 295, 325, 325), fill = "black")
    canvas.create_oval((375, 295, 405, 325), fill = "black")

    #Row 1
    canvas.create_oval((15, 255, 45, 285), fill = "black")
    canvas.create_oval((95, 255, 125, 285), fill = "black")
    canvas.create_oval((175, 255, 205, 285), fill = "black")
    canvas.create_oval((255, 255, 285, 285), fill = "black")
    canvas.create_oval((335, 255, 365, 285), fill = "black")

def set_pieces_white():
    #Row 1
    canvas.create_oval((55, 135, 85, 165), fill = "white")
    canvas.create_oval((135, 135, 165, 165), fill = "white")
    canvas.create_oval((215, 135, 245, 165), fill = "white")
    canvas.create_oval((295, 135, 325, 165), fill = "white")
    canvas.create_oval((375, 135, 405, 165), fill = "white")
    
    #Row 2
    canvas.create_oval((15, 95, 45, 125), fill = "white")
    canvas.create_oval((95, 95, 125, 125), fill = "white")
    canvas.create_oval((175, 95, 205, 125), fill = "white")
    canvas.create_oval((255, 95, 285, 125), fill = "white")
    canvas.create_oval((335, 95, 365, 125), fill = "white")

    #Row 3
    canvas.create_oval((55, 55, 85, 85), fill = "white")
    canvas.create_oval((135, 55, 165, 85), fill = "white")
    canvas.create_oval((215, 55, 245, 85), fill = "white")
    canvas.create_oval((295, 55, 325, 85), fill = "white")
    canvas.create_oval((375, 55, 405, 85), fill = "white")

    #Row 4
    canvas.create_oval((15, 15, 45, 45), fill = "white")
    canvas.create_oval((95, 15, 125, 45), fill = "white")
    canvas.create_oval((175, 15, 205, 45), fill = "white")
    canvas.create_oval((255, 15, 285, 45), fill = "white")
    canvas.create_oval((335, 15, 365, 45), fill = "white")



create_board()
set_pieces_black()
set_pieces_white()

#root.mainloop()
