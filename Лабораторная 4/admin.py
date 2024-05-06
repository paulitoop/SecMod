from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import os
import shutil



curr_path = ""
def empty():
    print("Hello world!")
    matrix.config(state=NORMAL)
    matrix.insert(END, "+ ")
    matrix.config(state=DISABLED)
    return 0

class SecurityManager:
    def __init__(self):
        self.folder_levels ={}
        self.security_levels = {}  # Словарь для хранения уровней секретности
        SecurityManager.read_levels(self)
        FolderManager.read_security_levels(self)
        if 'public' not in self.security_levels:
            self.security_levels['public'] = 1
            SecurityManager.write_levels(self)
        

    def create_security_level(self, name, level):
        if name not in self.security_levels:
            self.security_levels[name] = level
            SecurityManager.write_levels(self)
            SecurityManager.update(self)
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' создан успешно.")
        else:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем уже существует.")

    def update(self):
        SecurityManager.read_levels(self)
        SecurityManager.show_levels(self)
        FolderManager.read_levels(self)
        FolderManager.read_security_levels(self)

    def change_security_level(self, name, new_name, level):
        if name != new_name:
            if name in self.security_levels:
                self.security_levels[new_name] = level
                del self.security_levels[name]
                SecurityManager.write_levels(self)
                FolderManager.read_security_levels(self)
                for folder, level in self.folder_levels.items():
                    if level == name:
                        self.folder_levels[folder] = new_name
                FolderManager.write_security_levels(self)
                FolderManager.show_levels(self)
                SecurityManager.write_levels(self)
                SecurityManager.update(self)
                

                messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' изменен на '{new_name}' успешно.")
                
            else:
                messagebox.showerror("Ошибка", "Уровень секретности с таким именем отсутствует.")
        else:
            self.security_levels[new_name] = level
            SecurityManager.write_levels(self)
            SecurityManager.update(self)
        
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' изменен на '{new_name}' успешно.")
        
    
    def del_security_level(self,name):
        if name in self.security_levels:
            del self.security_levels[name]
            FolderManager.read_security_levels(self)
            for folder, level in self.folder_levels.items():
                if level == name:
                    self.folder_levels[folder] = "public"
            FolderManager.write_security_levels(self)
            FolderManager.show_levels(self)
            SecurityManager.write_levels(self)
            SecurityManager.update(self)
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' удален успешно.")
        else:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем отсутствует.")
    
    def security_level_dialog(self, option):
        print(self.folder_levels)
        name = simpledialog.askstring(f"{option} уровень секретности", "Введите название уровня секретности:", parent=window)
        if SecurityManager.validate_name(self, name, option):
            if option=="Удалить":
                SecurityManager.del_security_level(self,name)
                return 0
            if option=="Изменить":
                new_name = simpledialog.askstring(f"Изменить уровень секретности", "Введите новое название уровня секретности:", parent=window)
                if SecurityManager.validate_name(self, new_name, option):
                    level = simpledialog.askinteger(f"{option} уровень секретности", "Выберите уровень секретности (от 1 до 15):", minvalue=1, maxvalue=15,parent=window)
                    if level: 
                        SecurityManager.change_security_level(self,name,new_name, level)
            if option=="Создать":
                    level = simpledialog.askinteger(f"{option} уровень секретности", "Выберите уровень секретности (от 1 до 15):", minvalue=1, maxvalue=15,parent=window)
                    if level: 
                        SecurityManager.create_security_level(self,name, level)

    def validate_name(self, name, option):
        if name == 'public':
            messagebox.showerror("Ошибка", "Нельзя редактировать уровень 'public'.")
            return False
        elif (name in self.security_levels) and (option=="Создать"):
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем занят")
            return False
        elif name and all(c.isalnum() or c == '_' for c in name):
            return True
        else:
            messagebox.showerror("Ошибка", "Имя уровня секретности должно содержать только буквы, цифры и подчеркивания.")
            return False
        
    def write_levels(self):
        with open("levels.txt", "w") as file:
            for name, level in self.security_levels.items():
                file.write(f"{name}:{level}\n")

    def read_levels(self):
        if not os.path.exists("levels.txt"):
            file = open("levels.txt", "w")
            file.close()
        with open("levels.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                name = parts[0]
                level = int(parts[1])
                self.security_levels[name] = level
    
    def show_levels(self):
        ListLevels.config(state=NORMAL)
        ListLevels.delete("1.0", END)
        for name, level in self.security_levels.items():
            ListLevels.insert(END, f"{name} : {level}\n")
        ListLevels.config(state=DISABLED)


class FolderManager:
    
    def __init__(self, ListFiles):
        global curr_path
        self.rootDir = FolderManager.get_root_dir(self)
        self.folder_levels = {}
        self.security_levels = {}
        self.listbox = ListFiles
        curr_path = self.rootDir
        self.CopyPath = ""
        self.PastePath = ""
        FolderManager.show_files(self, self.rootDir, self.listbox)
        FolderManager.fill_folder_levels(self.rootDir, "folder_levels.txt")
        FolderManager.read_security_levels(self)
        FolderManager.read_levels(self)
        FolderManager.show_levels(self)

    def copy_files(self):
        FolderManager.read_security_levels(self)
        selection = ListFiles.curselection()
        if selection:
            folderName = ListFiles.get(selection[0])
            self.CopyPath = os.path.join(curr_path, folderName)
            # if os.path.isdir(fullPath):
            #     print("Папка")
            # if os.path.isfile(fullPath):
            #     print("Файл")
            rel_path = os.path.relpath( self.CopyPath,self.rootDir)
            mas = rel_path.split("\\")
            lv_max = 1
            if len(mas) != 1:
                for i in range(len(mas)):
                    st = str(mas[0])
                    for k in range(1,i+1):
                        st += "\\"
                        st += str(mas[k])
                    
                    print(st) 
                    level_name = self.folder_levels[st]
                    lavel_value = self.security_levels[level_name]
                    if lv_max < lavel_value:
                        lv_max = lavel_value
                    

            lavel_value = lv_max
            print(lavel_value)
           
            # level_name = self.folder_levels[rel_path]
            # lavel_value = self.security_levels[level_name]
            
            #print(level_name, lavel_value)
            messagebox.showinfo("Копирование", "Выбирете папку назначения\nи нажмите 'Копировать сюда'")
            folders_files = []
            self.listbox.delete(0, tk.END)
            for name in self.folder_levels:
                if name != rel_path:
                    if lavel_value <= self.security_levels[self.folder_levels[name]]:
                        folders_files.append(name)
            #print(folders_files)
            for item in folders_files:
                self.listbox.insert(tk.END, item)
        else:
            messagebox.showerror("Ошибка", "Выберите папку или файл для копирования")
            return None

    def make_copy(self):
        
        selection = ListFiles.curselection()
        if selection:
            folderName = ListFiles.get(selection[0])
            self.PastePath = os.path.join(self.rootDir, folderName)
            rel_path = os.path.relpath( self.PastePath,self.rootDir)
            level_name = self.folder_levels[rel_path]
            lavel_value = self.security_levels[level_name]

            for root, dirs, files in os.walk(self.CopyPath):
                for dir_name in dirs:
                    src_dir_path = os.path.join(root, dir_name)
                    dst_dir_path = os.path.join(self.PastePath, os.path.relpath(src_dir_path, self.CopyPath))
                    rel_src_dir_path = os.path.relpath(src_dir_path, self.rootDir)
                    tmp_level_name = self.folder_levels[rel_src_dir_path]
                    tmp_lavel_value = self.security_levels[tmp_level_name]
                    if tmp_lavel_value <=lavel_value:
                        shutil.copytree(src_dir_path, dst_dir_path)
                        tmp_rel_path = os.path.relpath(dst_dir_path, self.rootDir)
                        tmp_rel_copy_path = os.path.relpath(src_dir_path, self.rootDir)
                        self.folder_levels[tmp_rel_path] = self.folder_levels[tmp_rel_copy_path]
                        FolderManager.write_security_levels(self)
                        FolderManager.update(self)
                        print(tmp_rel_path, tmp_lavel_value)

            FolderManager.show_files(self, curr_path, self.listbox)
        else:
            messagebox.showerror("Ошибка", "Выберите папку или файл для копирования")
            FolderManager.show_files(self, curr_path, self.listbox)
            return None
        
    def read_levels(self):
        if not os.path.exists("levels.txt"):
            file = open("levels.txt", "w")
            file.close()
        with open("levels.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                name = parts[0]
                level = int(parts[1])
                self.security_levels[name] = level

    def read_security_levels(self):
        with open("folder_levels.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                name = parts[0]
                level = parts[1]
                self.folder_levels[name] = level

    def write_security_levels(self):
        with open("folder_levels.txt", "w") as file:
            for name, level in self.folder_levels.items():
                file.write(f"{name}:{level}\n")

    def update(self):
        FolderManager.write_security_levels(self)
        FolderManager.read_security_levels(self)
        FolderManager.show_levels(self)

    def show_levels(self):
        FilesLevels.config(state=NORMAL)
        FilesLevels.delete("1.0", END)
        for name, level in self.folder_levels.items():
            FilesLevels.insert(END, f"{name} : {level}\n")
        FilesLevels.config(state=DISABLED)

    def create_new_folder(self,name):
        global curr_path
        level = "public"
        root_dir = self.rootDir
        new_folder_path = os.path.join(curr_path, name)  # Полный путь к новой папке
        try:
            os.mkdir(new_folder_path)  # Создаем новую папку
            messagebox.showinfo("Уведомление", f"Папка '{name}' с уровнем '{level}' успешно создана")
            FolderManager.show_files(self, curr_path, self.listbox)
            with open("folder_levels.txt", 'a+') as f:
                rel_dir_path = os.path.relpath(new_folder_path, root_dir)
                f.write(f"{rel_dir_path}:public\n")
            FolderManager.read_security_levels(self)
            FolderManager.show_levels(self)
            print("Данные успешно записаны в файл folder_levels.txt.")
            return 0
        except OSError as e:
            messagebox.showerror("Ошибка", f"Ошибка при создании папки '{name}' в директории '{curr_path}': {e}")
            return None
        

    def del_folder(self):
        selection = ListFiles.curselection()
        if selection:
            folderName = ListFiles.get(selection[0])
            fullPath = os.path.join(curr_path, folderName)
            confirmed = messagebox.askyesno("Подтверждение", "Вы уверены, что хотите удалить папку?")
            if confirmed:   
                try:
                    rel_path = os.path.relpath(fullPath, self.rootDir)
                    self.folder_levels.pop(rel_path)
                    FolderManager.update(self)
                    
                    os.rmdir(fullPath)
                    messagebox.showinfo("Успех", "Папка удалена")
                except OSError as e:
                    messagebox.showerror("Ошибка", "Папка должна быть пустой")
            else:
                messagebox.showinfo("Информация", "Удаление отменено")
        else:
            messagebox.showerror("Ошибка", "Выберите папку")
            return None
        FolderManager.show_files(self, curr_path, self.listbox)

    def change_folder_name(self):
        print(self.security_levels)
        FolderManager.read_security_levels(self)
        FolderManager.read_levels(self)
        selection = ListFiles.curselection()
        if selection:
            folderName = ListFiles.get(selection[0])
            fullPath = os.path.join(curr_path, folderName)
            new_name = simpledialog.askstring(f"Изменить название папки", "Введите новое название папки", parent=window)
            if FolderManager.validate_name(self, new_name):
                level = simpledialog.askstring(f"Изменить название папки", "Выберите уровень секретности:",parent=window)
                if level in self.security_levels:
                    new_path = os.path.join(curr_path, new_name)
                    os.rename(fullPath,  new_path)
                    rel_old_path = os.path.relpath(fullPath, self.rootDir)
                    rel_new_path = os.path.relpath(new_path, self.rootDir)
                    print(rel_old_path)
                    print(rel_new_path)
                    self.folder_levels[rel_new_path] = self.folder_levels.pop(rel_old_path)
                    self.folder_levels[rel_new_path] = level
                    FolderManager.update(self)
                    messagebox.showinfo("Информация", "Папка изменена успешно")
                    FolderManager.show_files(self, curr_path, self.listbox)
                else:
                    print(self.security_levels)
                    messagebox.showerror("Ошибка", "Уровень секретности не существует")
                    return None

        else:
            messagebox.showerror("Ошибка", "Выберите папку")
            return None


    def create_folder_dialog(self, option):
        print(self.security_levels)
        print(self.folder_levels)
        levelsList = list(self.security_levels.keys())
        global curr_path
        if option=="Удалить":
            FolderManager.del_folder(self)
        if option=="Изменить":
            FolderManager.change_folder_name(self)
        if option=="Создать":
            name = simpledialog.askstring(f"{option} папку", "Введите название папки:", parent=window)
            if FolderManager.validate_name(self, name):
                FolderManager.create_new_folder(self,name)


    def validate_name(self, name):
        if name in self.security_levels:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем занят")
            return False
        elif name and all(c.isalnum() or c == '_' or c ==' ' for c in name):
            return True
        else:
            messagebox.showerror("Ошибка", "Имя уровня секретности папки должно содержать только буквы, цифры и подчеркивания.")
            return False


    def show_files(self, path, listbox):
        folders_files = []
        listbox.delete(0, tk.END)
        for name in os.listdir(path):
            rel_path = os.path.relpath(os.path.join(path, name), path)
            folders_files.append(rel_path)
        for item in folders_files:
            listbox.insert(tk.END, item)

    def get_root_dir(self):
        current_file = os.path.abspath(__file__)
        root_dir = os.path.dirname(current_file)
        
        return "c:\\Users\\pashc\\Desktop\\Уник\\Модели безопасности КС\\Лабораторная 4"

    def go_back(self):
        global curr_path
        #current_path = folder_manager.current_path
        if curr_path == self.rootDir:  # Если текущий путь - корневая директория
            messagebox.showinfo("Информация", "Вы уже в корневой директории.")
            return -1
        parent_path = os.path.dirname(curr_path)  # Получаем путь к родительской директории
        curr_path = parent_path
        spl = curr_path.split("Лабораторная 4")
        print(spl)
        if spl[1]=="":
            spl[1]="\\"
        LabelPath["text"] = spl[1]
        folder_manager.show_files(parent_path, ListFiles)

    def fill_folder_levels(root_dir, levels_file):
        if not os.path.exists("folder_levels.txt"):
            file = open("folder_levels.txt", "w")
            file.close()

        if os.path.getsize(levels_file) > 0:
            print("Файл folder_levels.txt уже содержит данные.")
            return
        with open(levels_file, 'w') as f:
            for root, dirs, files in os.walk(root_dir):
                # rel_path = os.path.relpath(root, root_dir)
                # f.write(f"{rel_path}:1\n")
                for dir_name in dirs:
                    dir_path = os.path.join(root, dir_name)
                    rel_dir_path = os.path.relpath(dir_path, root_dir)
                    f.write(f"{rel_dir_path}:public\n")
        print("Данные успешно записаны в файл folder_levels.txt.")

def on_double_click( event):
    global curr_path
    root_dir = folder_manager.get_root_dir()
    selection = ListFiles.curselection()  # Получаем индекс выбранного элемента
    if selection:  # Если есть выбранный элемент
        index = selection[0]  # Получаем первый выбранный индекс (если множественный выбор)
        folder_name = ListFiles.get(index)  # Получаем текст элемента (имя папки)
        full_path = os.path.join(curr_path, folder_name)
        if not os.path.isdir(full_path):  # Проверяем, является ли путь папкой
            messagebox.showerror("Ошибка", "Выбранный элемент не явялется папкой.")
            return -1
        print("Полный путь к выбранной папке:", full_path)
        curr_path= full_path
    spl = full_path.split("Лабораторная 4")
    print(spl)
    LabelPath["text"] = spl[1]
    folder_manager.show_files(full_path, ListFiles)




if __name__=="__main__":
    
    
    window = Tk()
    window.title("Панель управления")
    window.geometry('600x500')
    window.resizable(False, False)
    window.configure(background="#b2b6db")
  

    for i in range(2): window.columnconfigure(index=i,weight=1)
    for i in range(4): window.rowconfigure(index=i, weight=1)

    

    #Уровни секретности
    CreateLevel = Button(window, text = 'Создать уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Создать"))
    CreateLevel.place(x=10,y=10,width=126,height=35)
    ChangeLevel = Button(window, text = 'Изменить уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Изменить"))
    ChangeLevel.place(x=10,y=60,width=126,height=35)
    DelLevel = Button(window, text = 'Удалить уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Удалить"))
    DelLevel.place(x=10, y = 110,width=126,height=35)
    

    #Папки мамки
    CreateFolder = Button(window, text = 'Создать папку', command = lambda:folder_manager.create_folder_dialog("Создать"))
    CreateFolder.place(x=460,y=10,width=126,height=35)
    ChangeFolder = Button(window, text = 'Изменить папку', command = lambda:folder_manager.create_folder_dialog("Изменить"))
    ChangeFolder.place(x=460,y=60,width=126,height=35)
    DelFolder = Button(window, text = 'Удалить папку', command = lambda:folder_manager.create_folder_dialog("Удалить"))
    DelFolder.place(x=460,y=110,width=126,height=35)

    #Копирование папок
    CopyFolder = Button(window, text = 'Копировать файлы', command = lambda:folder_manager.copy_files())
    CopyFolder.place(x=240,y=10,width=126,height=35)

    #Подтверждение копирования
    CopyFolder = Button(window, text = 'Копировать сюда', command = lambda:folder_manager.make_copy())
    CopyFolder.place(x=240,y=60,width=126,height=35)

    BackButton = Button(window, text = 'Назад', command = lambda:folder_manager.go_back())
    BackButton.place(x=240,y=110,width=126,height=35)

    #Дирректории
    ListFiles = tk.Listbox(window)
    ListFiles.config(font=("consolas", 12))
    ListFiles.place(x=10,y=190,width=570,height=111)
    ListFiles.bind("<Double-Button-1>", on_double_click)

    #Уровни доступа
    ListLevels=Text(window)
    ListLevels.place(x=10,y=330,width=242,height=151)

    #Урвони папок
    FilesLevels=Text(window)
    FilesLevels.place(x=340,y=330,width=242,height=151)

    LabelLevels=tk.Label(window, bg="#b2b6db")
    LabelLevels["text"] = "Уровни доступа"
    LabelLevels.place(x=80,y=300,width=114,height=30)

    LabelLevelFolders=tk.Label(window, bg="#b2b6db")
    LabelLevelFolders["text"] = "Уровни папок"
    LabelLevelFolders.place(x=410,y=300,width=116,height=30)

    LabelFileSystem=tk.Label(window, bg="#b2b6db")
    LabelFileSystem["text"] = "Файловая система"
    LabelFileSystem.place(x=10,y=160,width=119,height=30)

    LabelPath=tk.Label(window, bg="#b2b6db")
    LabelPath["text"] = "\\"
    
    LabelPath.place(x=240,y=160,width=342,height=30)

    folder_manager = FolderManager(ListFiles)
    sec_manager = SecurityManager()
    sec_manager.show_levels()
    mainloop()