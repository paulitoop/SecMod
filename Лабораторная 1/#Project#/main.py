import os
import shutil
from tkinter import *
from tkinter import ttk
def create_file(file_name):
    direct = "..//Private"
    file = open(direct+"\\"+file_name, 'w+')
    file.write("Hello World!!!!!!!!!!!!!!!!")
    print(f"Файл {file_name} был успешно создан!")
    file.close()
    return 0


def move_file(file_name, mode):
    files = os.listdir("../Private")
    if mode == "2":
        shutil.copytree("..//Private", "..//Public", dirs_exist_ok = True)
        print("Файлы успешно перенесены!")
        return 0
    elif mode == "1":
        idFile = input("Введите номер файла: ")
        if idFile.isdigit() == 0:
            print("Неверный номер файла!")
            return -1
        if int(idFile) <= len(files):
            shutil.copy("..//Private\\"+files[int(idFile)-1], "..//Public")
            print(f"Файл {files[int(idFile)-1]} успешно перенесен!")
            return 0
        else:
            print("Некоректный номер файла!")
        return 0
    else:
        print("Некорректный параметр переноса!")
        return 1



if __name__ == '__main__':

    mw = Tk()
    mw.title("Users's programm")
    mw.geometry('700x300+400+200')
    mw.configure(background="#66CDAA")
    mw.resizable(False, False)
    mw.iconbitmap(default="userIco.ico")

    for i in range(3): mw.columnconfigure(i,weight=1)
    for i in range(8): mw.rowconfigure(i, weight=1)
    label1 = Label(text = "Hello world!")
    label1.pack()

    mw.mainloop()


    # columns = shutil.get_terminal_size().columns
    # print("==========".center(columns))
    # print("Добро пожаловать в программу для создания и копирования файлов!".center(columns))
    # print("==========".center(columns))
    # while True:
    #     columns = shutil.get_terminal_size().columns
    #
    #     print("\n-----")
    #     print("1. Создать файл\n2. Перенести файлы в общую папку\n0. Выйти из программы\n")
    #     mode =input("Введите операцию: ")
    #     print()
    #     if mode == "1":
    #         path = input("Введите имя файла: ")
    #         create_file(path+".txt")
    #     elif mode == "2":
    #         files = os.listdir("..//Private")
    #         i = 1
    #
    #         print("Список файлов:")
    #         for file in files:
    #
    #             print(f"{i}. {file}")
    #             i+=1
    #         print("\n-----")
    #         flag = input("Введите параметр переноса:\n1. Выбрать файл\n2. Перенести все\n")
    #         move_file("test.txt", flag)
    #     elif mode == "0":
    #         break
    #     else:
    #         print("Некорректная операция!\n")
    #         continue


