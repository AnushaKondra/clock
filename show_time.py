from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def show_time():
    string = strftime('%H:%M:%S %p')
    label.config(text = string)
    label .after(1000,show_time)   

label = Label(root,font = ("ds-digital",80), background = "black",foreground = "pink")
label.pack(anchor='center')
show_time()

mainloop()
