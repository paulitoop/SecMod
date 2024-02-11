import os
import shutil
from tkinter import *
from tkinter import ttk

init_scanning = False

def timed_checker(status=None):
    global init_scanning
    if status == "start":
        init_scanning = True
        st_but["text"] = "Сканнер\nзапущен"
    if status == "stop":
        init_scanning = False
        st_but["text"] = "Запустить\n сканнер"
    if init_scanning == True:
        shutil.copytree("../Public", "../Intruder", dirs_exist_ok=True)
        public_listbox.after(1000, timed_checker)
    return 0


def move_all():
    shutil.copytree("../Public", "../Intruder", dirs_exist_ok = True)
    return 0

def update_file_list(listbox, directory_path):
    file_list = os.listdir(directory_path)
    listbox.delete(0, END)
    for file in file_list:
        listbox.insert(END, file)
    window.after(1000, update_file_list, listbox, directory_path)  # Проверяем каждую секунду

if __name__ == '__main__':
    
    window = Tk()  
    window.title("Attacker's window")  
    window.geometry('700x300')
    window.configure(bg='#4B0082')
    window.iconphoto(False, PhotoImage(file="anon.png"))
    window.resizable(width=False, height=False)

    for i in range(3): window.columnconfigure(index=i, weight=1)
    for i in range(8): window.rowconfigure(index=i, weight=1)

    label_public = Label(text = "Публичная папка",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_public.grid(row=0, column=0)
    label_button = Label(text = "Выберете действие",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_button.grid(row=1, column=1)
    label_intr = Label(text = "Папка злоумышленника",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_intr.grid(row=0, column=2)
    
    public_listbox = Listbox(yscrollcommand=True)
    public_listbox.grid(row=1, column=0, rowspan=6)
    intr_listbox = Listbox(yscrollcommand=True)
    intr_listbox.grid(row=1, column=2, rowspan=6)
    update_file_list(public_listbox, "../Public")
    update_file_list(intr_listbox, "../Intruder")

    ttk.Button(text="Перенести\n      все",command =move_all).grid(row=2, column=1, padx=2, pady=2)

    st_but = ttk.Button(text="Запустить\n сканнер",\
               command =lambda: timed_checker("start"))
    st_but.grid(row=3, column=1, padx=2, pady=2)
    ttk.Button(text="Остановить\n  сканнер",\
               command =lambda: timed_checker("stop")).grid(row=4, column=1, padx=2, pady=2)
    

    mainloop()
    

   
            
            
        
    

