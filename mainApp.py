#       Imports         #
#Tkinter is our GUI manager
import tkinter as tk
from tkinter import *
#os handles operating system functionalities
import os
#picking is used for serializing Python objects
import pickle
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



#should be called last similar to JFrame
app.mainloop()
