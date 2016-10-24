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

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))


canvas.create_rectangle((10, 10, 50, 50), fill = "brown")
canvas.create_rectangle((90, 10, 130, 50), fill = "brown")
canvas.create_rectangle((50, 50, 90, 90), fill = "brown")
canvas.create_rectangle((130, 50, 170, 90), fill = "brown")
canvas.create_rectangle((170, 10, 210, 50), fill = "brown")
canvas.create_rectangle((210, 50, 250, 90), fill = "brown")
canvas.create_rectangle((250, 10, 290, 50), fill = "brown")
canvas.create_rectangle((290, 50, 330, 90), fill = "brown")

canvas.create_rectangle((10, 90, 50, 130), fill = "brown")
canvas.create_rectangle((90, 90, 130, 130), fill = "brown")
canvas.create_rectangle((50, 130, 90, 170), fill = "brown")
canvas.create_rectangle((130, 130, 170, 170), fill = "brown")
canvas.create_rectangle((170, 90, 210, 130), fill = "brown")
canvas.create_rectangle((210, 130, 250, 170), fill = "brown")
canvas.create_rectangle((250, 90, 290, 130), fill = "brown")
canvas.create_rectangle((290, 130, 330, 170), fill = "brown")

canvas.create_rectangle((10, 170, 50, 210), fill = "brown")
canvas.create_rectangle((90, 170, 130, 210), fill = "brown")
canvas.create_rectangle((50, 210, 90, 250), fill = "brown")
canvas.create_rectangle((130, 210, 170, 250), fill = "brown")
canvas.create_rectangle((170, 170, 210, 210), fill = "brown")
canvas.create_rectangle((210, 210, 250, 250), fill = "brown")
canvas.create_rectangle((250, 170, 290, 210), fill = "brown")
canvas.create_rectangle((290, 210, 330, 250), fill = "brown")

canvas.create_rectangle((10, 250, 50, 290), fill = "brown")
canvas.create_rectangle((90, 250, 130, 290), fill = "brown")
canvas.create_rectangle((50, 290, 90, 330), fill = "brown")
canvas.create_rectangle((130, 290, 170, 330), fill = "brown")
canvas.create_rectangle((170, 250, 210, 290), fill = "brown")
canvas.create_rectangle((210, 290, 250, 330), fill = "brown")
canvas.create_rectangle((250, 250, 290, 290), fill = "brown")
canvas.create_rectangle((290, 290, 330, 330), fill = "brown")

canvas.create_line(10, 10, 330, 10, fill='black', width=1)
canvas.create_line(10, 10, 10, 330, fill='black', width=1)
canvas.create_line(330, 10, 330, 330, fill='black', width=1)
canvas.create_line(10, 330, 330, 330, fill='black', width=1)

##canvas.create_line(10, 10, 250, 10, fill = 'black')
##canvas.create_line(10, 40, 250, 40, fill = 'black')
##canvas.create_line(10, 70, 250, 70, fill = 'black')
##canvas.create_line(10, 100, 250, 100, fill = 'black')
##canvas.create_line(10, 130, 250, 130, fill = 'black')
##canvas.create_line(10, 160, 250, 160, fill = 'black')
##canvas.create_line(10, 190, 250, 190, fill = 'black')
##canvas.create_line(10, 220, 250, 220, fill = 'black')
##canvas.create_line(10, 250, 250, 250, fill = 'black')
##
##canvas.create_line(10, 10, 10, 250, fill = 'black')
##canvas.create_line(40, 10, 40, 250, fill = 'black')
##canvas.create_line(70, 10, 70, 250, fill = 'black')
##canvas.create_line(100, 10, 100, 250, fill = 'black')
##canvas.create_line(130, 10, 130, 250, fill = 'black')
##canvas.create_line(160, 10, 160, 250, fill = 'black')
##canvas.create_line(190, 10, 190, 250, fill = 'black')
##canvas.create_line(220, 10, 220, 250, fill = 'black')
##canvas.create_line(250, 10, 250, 250, fill = 'black')

#root.mainloop()
