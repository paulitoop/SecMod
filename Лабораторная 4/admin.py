from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def empty():
    print("Hello world!")
    matrix.config(state=NORMAL)
    matrix.insert(END, "+ ")
    matrix.config(state=DISABLED)
    return 0

class SecurityManager:
    def __init__(self):
        self.security_levels = {}  # Словарь для хранения уровней секретности
        SecurityManager.read_levels(self)

    def create_security_level(self, name, level):
        if name not in self.security_levels:
            self.security_levels[name] = level
            SecurityManager.write_levels(self)
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' создан успешно.")
        else:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем уже существует.")

    def change_security_level(self, name, new_name, level):
        if name in self.security_levels:
            self.security_levels[new_name] = level
            del self.security_levels[name]
            SecurityManager.write_levels(self)
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' изменен на '{new_name}' успешно.")
        else:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем отсутствует.")
    
    def del_security_level(self,name):
        if name in self.security_levels:
            
            del self.security_levels[name]
            SecurityManager.write_levels(self)
            messagebox.showinfo("Уведомление", f"Уровень секретности '{name}' удален успешно.")
        else:
            messagebox.showerror("Ошибка", "Уровень секретности с таким именем отсутствует.")
    
    def security_level_dialog(self, option):
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
        with open("levels.txt", "r") as file:
            for line in file:
                parts = line.strip().split(":")
                name = parts[0]
                level = int(parts[1])
                self.security_levels[name] = level
    
    def show_levels(self):
        matrix.config(state=NORMAL)
        matrix.delete("1.0", END)
        for name, level in self.security_levels.items():
            matrix.insert(END, f"{name}:{level}\n")
        matrix.config(state=DISABLED)


if __name__=="__main__":
    sec_manager = SecurityManager()

    window = Tk()
    window.title("Панель управления")
    window.geometry('800x600')
    window.resizable(False, False)
    window.configure(background="#b2b6db")
  

    for i in range(8): window.columnconfigure(index=i,weight=1)
    for i in range(4): window.rowconfigure(index=i, weight=1)

    #Уровни секретности
    CreateLevel = Button(window, text = 'Создать уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Создать"))
    CreateLevel.grid(row = 0, column = 0)
    ChangeLevel = Button(window, text = 'Изменить уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Изменить"))
    ChangeLevel.grid(row = 1, column = 0)
    DelLevel = Button(window, text = 'Удалить уровень\nсекретности', command = lambda:sec_manager.security_level_dialog("Удалить"))
    DelLevel.grid(row = 2, column =0)
    ShowLevels = Button(window, text = 'Показать уровни\nсекретности', command = lambda:sec_manager.show_levels())
    ShowLevels.grid(row = 3, column =0)

    #Папки мамки
    CreateFolder = Button(window, text = 'Создать папку', command = lambda:empty())
    CreateFolder.grid(row = 0, column = 1)
    ChangeFolder = Button(window, text = 'Изменить уровень\nпапки', command = lambda:empty())
    ChangeFolder.grid(row = 1, column = 1)
    DelFolder = Button(window, text = 'Удалить папку', command = lambda:empty())
    DelFolder.grid(row = 2, column =1)

    #Копирование папок
    CopyFolder = Button(window, text = 'Копировать файлы', command = lambda:empty())
    CopyFolder.grid(row = 1, column = 2)

    #Вывод инфы
    matrix = tk.Text(borderwidth=3, relief="sunken",height=10, width=60)
    matrix.config(font=("consolas", 12), undo=True, wrap=NONE,state=DISABLED)
    matrix.grid(row=3, column=1, padx=1, pady=1)

    
    mainloop()