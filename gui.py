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
editMenu=Menu(fileMenu)
fileMenu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Edit File",command=addProject)
#Adding A Toolbar to the GUI
toolbar=Frame(root,bg="Pink")
insertButton=Button(toolbar,text="Print",command=addProject)
insertButton.pack(side=LEFT,padx=2,pady=3)
printButton=Button(toolbar,text="Print",command=addProject)
printButton.pack(padx=2,pady=3)
toolbar.pack()
root.mainloop()