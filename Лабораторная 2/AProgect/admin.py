import os
import shutil
from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    
    window = Tk()  
    window.title("Admin's window")  
    window.geometry('700x700')
    window.configure(bg='#4B0082')
    window.resizable(width=False, height=False)

    for i in range(3): window.columnconfigure(index=i, weight=1)
    for i in range(8): window.rowconfigure(index=i, weight=1)

    mainloop()
    

   
            
            
        
    

