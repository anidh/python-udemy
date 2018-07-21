from tkinter import *

#using Menu Demo Here
def addProject():
    print("Menu Item Clicked!")
root=Tk()
fileMenu=Menu(root)
root.config(menu=fileMenu)
fileSubMenu=Menu(fileMenu)
fileMenu.add_cascade(label="File",menu=fileSubMenu)
fileSubMenu.add_command(label="New Project...",command=addProject)
fileSubMenu.add_command(label="New...",command=addProject)
fileSubMenu.add_command(label="New Scratch File...",command=addProject)
fileSubMenu.add_separator()
openRecent=Menu(fileMenu)
openRecent.add_command(label="recentFile...",command=addProject)
editMenu=Menu(fileMenu)
fileMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Edit File",command=addProject)
root.mainloop()