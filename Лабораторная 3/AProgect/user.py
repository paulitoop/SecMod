import os
import shutil
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb

login = ""
request = ""

def get_conf(path):
    file = open(path, "r")
    matrix = file.readlines()
    file.close()
    return matrix

def get_acces_matrix(matrix:list):
    acces_matrix = {}
    for line in matrix:
        user, permission = line.split("-")
        if permission[-1]=="\n":
            acces_matrix[user] = permission[:-1]
        else:
            acces_matrix[user] = permission
    return acces_matrix

def string_check():
    global login
    if login == "":
        mb.showerror("Ошибка", "Введите имя пользователя")
        return 1
    request = entryInput.get()

    config = get_conf("matrix.txt")
    acces_matrix = get_acces_matrix(config)
    permission = acces_matrix[login]
    result = ""
    for symbol in request:
        if symbol in set(permission):
            result+=symbol
    print(result)
    textOutput.delete("1.0", END)
    textOutput.insert("1.0", result)
    return result

def get_login():
    global login
    login = entryLogin.get()
    config = get_conf("matrix.txt")
    acces_matrix = get_acces_matrix(config)
    if login not in acces_matrix:
        mb.showerror("Ошибка", "Имя пользователя отсутствует в базе данных")
        return 2
    #permission = acces_matrix[login]
    #print(permission)
    if login== "":
        mb.showerror("Ошибка", "Введите имя пользователя")
        return 1
    elif not set("<>,\'\":;!_.*-+()/#¤%&?|\)").isdisjoint(login):
        mb.showerror("Ошибка", "Некорректное имя пользователя")
        return 2
    else:
        mb.showinfo("Успех", "Имя пользователя обновлено")
        return login


if __name__ == '__main__':

    config= get_conf("matrix.txt")
    acces_matrix = get_acces_matrix(config)

    mw = Tk()
    mw.title("Users's programm")
    mw.geometry('700x200')
    mw.configure(background="#66CDAA")
    mw.resizable(False, False)
    mw.iconbitmap(default="userIco.ico")

    for i in range(8): mw.columnconfigure(i,weight=1)
    for i in range(24): mw.rowconfigure(i, weight=1)

    labelLogin = Label(text = "Имя пользователя",background="#66CDAA", font=("Arial", 11))
    labelInput = Label(text = "Введите желаемые файлы",background="#66CDAA", font=("Arial", 11))
    labelOutput = Label(text = "Результат",background="#66CDAA", font=("Arial", 11))
    labelLogin.grid(row = 0, column=0)
    labelInput.grid(row = 2, column=0)
    labelOutput.grid(row = 4, column=0)

    entryLogin = Entry(width = 33)
    entryInput = Entry(width = 33)
    textOutput = Text(width=25, height=1)
    entryLogin.grid(row = 1, column=0)
    entryInput.grid(row = 3, column=0)
    textOutput.grid(row = 5, column=0)


    buttonLogin = Button(width=25, text="Ввод", command=lambda: get_login())
    buttonInput = Button(width=25, text="Ввод",command=lambda: string_check())
    buttonLogin.grid(row = 1, column = 1)
    buttonInput.grid(row = 3, column = 1)

    mw.mainloop()



# print(acces_matrix)
# print(acces_matrix["user1"])
# print(string_check("1253DAbvc", "user1", acces_matrix))


