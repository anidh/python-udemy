from tkinter import *
import tkinter.messagebox
root=Tk()
#Using Canvas On Tinkter
canvas=Canvas(root)
newLine=canvas.create_line(0,0,255,255)
otherLine=canvas.create_line(6,7,50,87)
canvas.pack()
root.mainloop()