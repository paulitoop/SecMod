import os
import shutil


def timed_checker(files):
    newfiles = os.listdir("Public")
    if newfiles != files:
        print("Created new file:")
        for file in newfiles:
            if not(file in newfiles):
                print(f"Created new file:{file}!")
    return newfiles

if __name__ == '__main__':
    files = os.listdir("Public")
    mode = input("ВЫберете что хотите сделать:\n1. Мониторинг директории Publiс\
                 \n2. Разовая проверка\nДля введите что-то иное\n")
    if mode == "1":
        while 1:
            flag = 0
            files = timed_checker(files)
            
            
        
    

