import os
import shutil
from tkinter import *
from tkinter import ttk

intr_files = os.listdir("../Intruder")
public_files = os.listdir("../IPublic")
init_scanning = False

def timed_checker(status=None):
    global intr_files, public_files, init_scanning
    dif = []
    if status == "start":
        init_scanning = True
        st_but["text"] = "Сканнер\nзапущен"
    if status == "stop":
        init_scanning = False
        st_but["text"] = "Запустить\n сканнер"

    if init_scanning == True:
        newfiles = os.listdir("../Public")
        if newfiles != public_files:
            for nfile in newfiles:
                flag = 0
                for file in public_files:
                    if nfile == file:
                        flag = 1
                if flag == 0:
                    dif.append(nfile)
        for i in dif:
            public_listbox.insert(0, i+" (новый)")
        public_files = newfiles
        public_listbox.after(1000, timed_checker)

    return 0


def move_all():
    global intr_files
    shutil.copytree("../Public", "../Intruder", dirs_exist_ok = True)
    newintr_files = os.listdir("../Intruder")
    dif = []
    for nfile in newintr_files:
        flag = 0
        for file in intr_files:
            if nfile == file:
                flag = 1
        if flag == 0:
            dif.append(nfile)
    for i in dif:
        intr_listbox.insert(0, i)
    
    intr_files = newintr_files
    
    return 0


if __name__ == '__main__':
    
    window = Tk()  
    window.title("Attacker's window")  
    window.geometry('700x300')
    window.configure(bg='#4B0082')
   
    window.resizable(width=False, height=False)
    for i in range(3): window.columnconfigure(index=i, weight=1)
    for i in range(8): window.rowconfigure(index=i, weight=1)

    label_public = Label(text = "Публичная папка",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_public.grid(row=0, column=0)
    label_button = Label(text = "Выберете действие",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_button.grid(row=1, column=1)
    label_intr = Label(text = "Папка злоумышленника",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_intr.grid(row=0, column=2)
    
    public_listbox = Listbox(listvariable=StringVar(value=public_files), yscrollcommand=True)
    public_listbox.grid(row=1, column=0, rowspan=6)
    intr_listbox = Listbox(listvariable=StringVar(value=intr_files))
    intr_listbox.grid(row=1, column=2, rowspan=6)

    ttk.Button(text="Перенести\n      все",command =move_all).grid(row=2, column=1, padx=2, pady=2)

    st_but = ttk.Button(text="Запустить\n сканнер",\
               command =lambda: timed_checker("start"))
    st_but.grid(row=3, column=1, padx=2, pady=2)
    ttk.Button(text="Остановить\n  сканнер",\
               command =lambda: timed_checker("stop")).grid(row=4, column=1, padx=2, pady=2)
    

    mainloop()
    

   
            
            
        
    

