import os
import shutil
from tkinter import *
from tkinter import ttk




if __name__ == '__main__':

    dirPr = "..//Private"
    dirPb = "..//Public"

    mw = Tk()
    mw.title("Users's programm")
    mw.geometry('700x700')
    mw.configure(background="#66CDAA")
    mw.resizable(False, False)
    mw.iconbitmap(default="userIco.ico")

    for i in range(3): mw.columnconfigure(i,weight=1)
    for i in range(8): mw.rowconfigure(i, weight=1)

    

    mw.mainloop()




