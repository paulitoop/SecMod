import os
import shutil


def create_file(file_name):
    direct = "Private"
    file = open(direct+"\\"+file_name, 'w+')
    file.write("Hello World!!!!!!!!!!!!!!!!")
    file.close()
    return 0


def move_file(file_name, mode):
    files = os.listdir("Private")

    if mode == "1":
        shutil.copytree("Private",
                        "Public",
                        dirs_exist_ok = True)
        return 0
    elif mode == "0":
        idFile = input("Введите номер файла: ")
        if idFile.isdigit() == 0:
            print("Неверный номер файла")
            return -1
        if int(idFile) > files:
            shutil.move("Private"+files[int(idFile)-1],
"Public")
        return 0
    else:
        print("Некорректный параметр переноса")
        return 1



if __name__ == '__main__':

    while True:
        print("Введите операцию:")

        mode = input("1. Создать файл\n2. Перенести файлы в общую папку\n0. Выйти из программы\n")

        if mode == "1":
            path = input("Введите имя файла: ")
            create_file(path+".txt")
        elif mode == "2":
            files = os.listdir("Private")
            i = 1
            for file in files:
                print(f"{i}. {file}")
                i+=1
            flag = input("Введите параметр переноса:\n0. Выбрать файл\n1. Перенести все\n")
            move_file("test.txt", flag)
        elif mode == "0":
            break
        else:
            print("Некорректная операция")
            continue


