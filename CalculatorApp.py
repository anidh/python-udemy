from tkinter import *
import parser
#Building the Calculator App
root=Tk()
root.title("Calculator")
#Adding Input Field
display=Entry(root)
display.grid(row=1,columnspan=6,sticky=W+E)
#Defining Function to Add Values To the Entry Field
i=0
def addEntry(num):
    global i
    display.insert(i,num)
    i+=1
#Function For Clear All
def clearAll():
    display.delete(0,END)
def clearSingle():
    theString=display.get()
    if len(theString)>0:
        newString=theString[:-1]
        clearAll()
        display.insert(0,newString)
    else:
        newString="Error"
        clearAll()
        display.insert(0,newString)
        clearAll()
def getOperator(operator):
    global i
    lengthO=len(operator)
    display.insert(i,operator)
    i+=lengthO
def calculateResult():
    value=display.get()
    try:
        interValue=parser.expr(value).compile()
        result=eval(interValue)
        clearAll()
        display.insert(i,result)
    except Exception:
        clearAll()
        display.insert(0,"ERROR")
def factorial():
    num=int(display.get())
    fact=1
    clearAll()
    if num<0:
        clearAll()
    elif num==0:
        display.insert(0,"1")
    else:
        for i in range(1,num+1):
            fact=fact*i
        display.insert(0,fact)


#Adding Buttons Row 1
Button(root,text="1",command=lambda :addEntry(1)).grid(row=2,column=0)
Button(root,text="2",command=lambda :addEntry(2)).grid(row=2,column=1)
Button(root,text="3",command=lambda :addEntry(3)).grid(row=2,column=2)
#Adding Buttons Row 2
Button(root,text="4",command=lambda :addEntry(4)).grid(row=3,column=0)
Button(root,text="5",command=lambda :addEntry(5)).grid(row=3,column=1)
Button(root,text="6",command=lambda :addEntry(6)).grid(row=3,column=2)
#Adding Buttons Row 3
Button(root,text="7",command=lambda :addEntry(7)).grid(row=4,column=0)
Button(root,text="8",command=lambda :addEntry(8)).grid(row=4,column=1)
Button(root,text="9",command=lambda :addEntry(9)).grid(row=4,column=2)
#Adding functional buttons
Button(root,text="AC",command=clearAll).grid(row=5,column=0)
Button(root,text="0",command=lambda :addEntry(0)).grid(row=5,column=1)
Button(root,text="=",command=calculateResult).grid(row=5,column=2)
#Adding Mathematical Buttons
Button(root,text="+",command=lambda :getOperator("+")).grid(row=2,column=3)
Button(root,text="-",command=lambda :getOperator("-")).grid(row=3,column=3)
Button(root,text="*",command=lambda :getOperator('*')).grid(row=4,column=3)
Button(root,text="/",command=lambda :getOperator("/")).grid(row=5,column=3)
#Adding More Functionalities
Button(root,text="Pi",command=lambda :getOperator("*3.14")).grid(row=2,column=4)
Button(root,text="%",command=lambda :getOperator("%")).grid(row=3,column=4)
Button(root,text="(",command=lambda :getOperator("(")).grid(row=4,column=4)
Button(root,text="exp",command=lambda :getOperator("**")).grid(row=5,column=4)
#-----
Button(root,text="<--",command=clearSingle).grid(row=2,column=5)
Button(root,text="!",command=factorial).grid(row=3,column=5)
Button(root,text=")",command=lambda :getOperator(")")).grid(row=4,column=5)
Button(root,text="^",command=lambda :getOperator("**2")).grid(row=5,column=5)
root.mainloop()