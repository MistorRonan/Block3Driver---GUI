#       Imports         #
#Tkinter is our GUI manager
import tkinter as tk
import pygame
from tkinter import *
from tkinter import colorchooser, filedialog, OptionMenu, messagebox
from tkinter import DOTBOX, StringVar, simpledialog
#os handles operating system functionalities
import os
#picking is used for serializing Python objects
import pickle
from tkinter.ttk import Combobox

#import local files
import testingImports as TI
#       Classes         #
class App(tk.Tk):
    def __init__(self):
        super().__init__()


#    Window Settings    #
app=App()
app.geometry("960x540")
app.title("WAYD Paint")


###         DEFINE VARIABLES        ###
prevPoint=[0, 0]
currentPoint=[0, 0]


maxSize = 10
minSize = 1
defaultSize = 4
brushSize=defaultSize
brushColor = "black"



##define functions
#tools
def pencil() :
    global brushColor,curcolor
    brushColor="black"
    canvas["cursor"]="pencil"
    curcolor = Canvas(curcolorf, height=32, width=32, bg=brushColor)
    pass
def eraser():
    global brushColor,curcolor
    brushColor = "white"
    canvas["cursor"] = DOTBOX
    curcolor = Canvas(curcolorf, height=32, width=32, bg=brushColor)

def colorChange():
    global brushColor, curcolor
    color = colorchooser.askcolor(title="Select a Color")
    canvas["cursor"] = "pencil"
    if color[1]:
        brushColor = color[1]
        curcolor = Canvas(curcolorf, height=32, width=32, bg=color[1])

    else:
        pass
#file functions
def saveImg():
    pass
def loadImg():
    pass
def newImg():
    pass
#brush tools
def incBrushSize():
    global brushSize,maxSize
    if(brushSize!=maxSize) :
        brushSize+=1
    pass
def decBrushSize():
    global brushSize,minSize
    if(brushSize!=minSize):
        brushSize-=1
    pass
def defBrushSize():
    global brushSize,defaultSize
    brushSize=defaultSize
    pass
#other
def clearCanvas():
    canvas.delete("all")
def exitProgram():
    pass

#canvas functions
def paint(event):
    global prevPoint
    global currentPoint

    x = event.x
    y = event.y

    currentPoint = [x, y]

    if prevPoint != [0, 0]:
        canvas.create_polygon(
            prevPoint[0],
            prevPoint[1],
            currentPoint[0],
            currentPoint[1],
            fill=brushColor,
            outline=brushColor,
            width=brushSize,
        )

    prevPoint = currentPoint

    if event.type == "5":
        prevPoint = [0, 0]



###Tools Frame
topframe = Frame(app,height=160,width=960)
topframe.grid(row=0,column=0)


##holder
holder = Frame(topframe,height=160,width=928,bg="white",padx=8,pady=0)
holder.grid(row=0,column=0,sticky=NW)
holder.place(relx=0.5,rely=0.55, anchor=CENTER)
#set up the columns for holder
columnsize = 72
columns = 5
for x in range(columns-1):
    holder.columnconfigure(x,minsize=columnsize)
holder.rowconfigure(0,minsize=24)

##set the file drop down menu
opts = ["Save","Load","New"]

dropmenu = Combobox(holder,values=opts,width=16,state="readonly")
dropmenu.set("File")
dropmenu.grid(row=0,column=0)

##set the tools menu
toollabel = Label(holder,text="Tools",borderwidth=2,relief=SOLID,width=16)
toollabel.grid(row=0,column=1)

#pencil
pencilButton = Button(holder,text="Pencil",height=1,width=12,command=pencil)
pencilButton.grid(row=1,column=1)
#eraser
easerButton = Button(holder,text="Eraser",height=1,width=12,command=eraser)
easerButton.grid(row=2,column=1)
#color change
colorButton = Button(holder,text="Color Change",height=1,width=12,command=colorChange)
colorButton.grid(row=3,column=1)

##set brush menu
brushlabel = Label(holder,text="Brush Size",borderwidth=2,relief=SOLID,width=16)
brushlabel.grid(row=0,column=2)

incButton = Button(holder,text="Increase",height=1,width=12,command=incBrushSize)
incButton.grid(row=1,column=2)

decButton=Button(holder,text="Decrease",height=1,width=12,command=decBrushSize)
decButton.grid(row=2,column=2)

resButton = Button(holder,text="Default",height=1,width=12,command=defBrushSize)
resButton.grid(row=3,column=2)
##other menu
otherlabel = Label(holder,text="Other",borderwidth=2,relief=SOLID,width=16)
otherlabel.grid(row=0,column=3)

clearButton = Button(holder,text="Clear Canvas",height=1,width=12,command=clearCanvas)
clearButton.grid(row=1,column=3)

####        CANVAS SETUP        ####
##init frame
canframe = Frame(app,width=960,height=500)
canframe.grid(row=1,column=0)
##create canvas
canvas = Canvas(canframe,height=450,width=960,bg="white")
canvas.grid(row=0,column=0)
canvas.place(relx=0.5,rely=0.5,anchor=CENTER)
canvas.config(cursor="pencil")

canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", paint)
canvas.bind("<Button-1>", paint)


##curcolor
curcolorf = Frame(app,width=32,height=32,padx=0,pady=0)
#curcolorf.grid(row=0,column=0,sticky=NW)
curcolorf.place(anchor=NW)
curcolor=Canvas(curcolorf,height=32,width=32,bg=brushColor)
curcolor.grid(row=0,column=0)
#should be called last similar to JFrame
app.mainloop()
