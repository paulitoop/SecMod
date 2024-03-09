import os
import shutil
from tkinter import *
from tkinter import ttk


def load_conf(path):
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

def string_check(request:str, login:str, acces_matrix:dict):
    permission = acces_matrix[login]
    resul = ""
    for symbol in request:
        if symbol in set(permission):
            resul+=symbol
    return resul

def login(user_name):
    if user_name == "":
        return 1
    elif not set("<>,\'\":;!_.*-+()/#¤%&?|\)").isdisjoint(user_name):
        return 2
    else:
        return user_name

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


config= load_conf("matrix.txt")
acces_matrix = get_acces_matrix(config)
print(acces_matrix)
print(acces_matrix["user1"])
print(string_check("1253DAbvc", "user1", acces_matrix))


