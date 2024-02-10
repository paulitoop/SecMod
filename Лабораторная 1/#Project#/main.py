import os
import shutil
from tkinter import *
from tkinter import ttk
def create_file(entry, listPr):
    direct = "..//Private"
    file_name = entry.get()
    if file_name == "" or not set(",:;!_*-+()/#¤%&)").isdisjoint(file_name) or file_name[0]=="." : return 1
    file = open(direct+"//"+file_name, 'w+')
    file.write("Hello World!!!!!!!!!!!!!!!!")
    file.close()
    update_file_list(listPr, "..//Private")
    entry.delete(0, END)
    listPr.selection_clear(0, END)
    return 0


def move_file(listPr, listPb, mode):
    if mode == 2:
        shutil.copytree("..//Private", "..//Public", dirs_exist_ok = True)
    elif mode == 1:
        for file in listPr.curselection():
            shutil.copy("..//Private//"+listPr.get(file), "..//Public")
    update_file_list(listPb, "..//Public")
    listPr.selection_clear(0, END)
    return 0


def update_file_list(listbox, directory_path):
    file_list = os.listdir(directory_path)
    listbox.delete(0, END)
    for file in file_list:
        listbox.insert(END, file)
   # mw.after(1000, update_file_list, listbox, directory_path)  # Проверяем каждую секунду

def hello(list):
    l = list.curselection()
    print(list.get(l))
    return 0
if __name__ == '__main__':

    dirPr = "..//Private"
    dirPb = "..//Public"

    mw = Tk()
    mw.title("Users's programm")
    mw.geometry('700x300+400+200')
    mw.configure(background="#66CDAA")
    mw.resizable(False, False)
    mw.iconbitmap(default="userIco.ico")

    for i in range(3): mw.columnconfigure(i,weight=1)
    for i in range(8): mw.rowconfigure(i, weight=1)

    # Создание надписей
    labelPrivate = Label(text = "Private folder", background= "#66CDAA",font =("Arial", 11))
    labelPrivate.grid(row=0,column=0)
    labelPublic = Label(text="Public folder", background="#66CDAA", font=("Arial", 11))
    labelPublic.grid(row=0, column=2)
    # Создание списка файлов публичной папки
    listPublic = Listbox(selectmode=EXTENDED, yscrollcommand="True",borderwidth=0, highlightthickness=0, background="#E0FFFF")
    listPublic.grid(row =1, column =2)
    listPublic.bindtags(("listPublic", "mw", "all"))
    update_file_list(listPublic, dirPb)
    # Создание списка файлов приватной папки
    listPrivate = Listbox(selectmode=EXTENDED, yscrollcommand="True", borderwidth=0, highlightthickness=0, background="#E0FFFF")
    listPrivate.grid(row=1, column=0)
    update_file_list(listPrivate, dirPr)


    # Настройка стиля для кнопок
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton',
                    background="#E0FFFF",
                    width=20,
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor='none')
    style.map('TButton', background=[('active', "#AFEEEE")])

    # Создание кнопки копирования всех файлов
    btCopyAll = ttk.Button(text = "Move all files", command=lambda: move_file(listPrivate, listPublic,2))
    btCopyAll.grid(row= 0,column = 1)
    # Создание кнопки копирвоания выделенного файла
    btCopySelect = ttk.Button(text="Move selected files", command=lambda: move_file(listPrivate, listPublic, 1))
    btCopySelect.grid(row=1, column=1, sticky="n")

    # Создание кнопки создания файла
    btCreateFile = ttk.Button(text="Create file", command=lambda: create_file(entry, listPrivate))
    btCreateFile.grid(row=5, column=1)
    # Создание поля для ввода имени файла
    entry = ttk.Entry(width = 25)
    entry.grid(row = 3, column=1,ipadx=2, ipady=2 )
    # Создание надписи к полю ввода имени
    labelNewName = Label(text="File name", background="#66CDAA", font=("Arial", 11))
    labelNewName.grid(row=4, column=1)

    mw.mainloop()




