import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Панель управления")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_559=tk.Button(root)
        GButton_559["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_559["font"] = ft
        GButton_559["fg"] = "#000000"
        GButton_559["justify"] = "center"
        GButton_559["text"] = "Создать уровень секретности"
        GButton_559.place(x=10,y=10,width=126,height=30)
        GButton_559["command"] = self.GButton_559_command

        GButton_995=tk.Button(root)
        GButton_995["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_995["font"] = ft
        GButton_995["fg"] = "#000000"
        GButton_995["justify"] = "center"
        GButton_995["text"] = "Изменить уровень секретности"
        GButton_995.place(x=10,y=60,width=126,height=30)
        GButton_995["command"] = self.GButton_995_command

        GButton_639=tk.Button(root)
        GButton_639["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_639["font"] = ft
        GButton_639["fg"] = "#000000"
        GButton_639["justify"] = "center"
        GButton_639["text"] = "Удалить уровень секретности"
        GButton_639.place(x=10,y=110,width=126,height=30)
        GButton_639["command"] = self.GButton_639_command

        GButton_426=tk.Button(root)
        GButton_426["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_426["font"] = ft
        GButton_426["fg"] = "#000000"
        GButton_426["justify"] = "center"
        GButton_426["text"] = "Создать папку"
        GButton_426.place(x=460,y=10,width=126,height=30)
        GButton_426["command"] = self.GButton_426_command

        GButton_306=tk.Button(root)
        GButton_306["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_306["font"] = ft
        GButton_306["fg"] = "#000000"
        GButton_306["justify"] = "center"
        GButton_306["text"] = "Изменить уровень папки"
        GButton_306.place(x=460,y=60,width=126,height=30)
        GButton_306["command"] = self.GButton_306_command

        GButton_760=tk.Button(root)
        GButton_760["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_760["font"] = ft
        GButton_760["fg"] = "#000000"
        GButton_760["justify"] = "center"
        GButton_760["text"] = "Удалить папку"
        GButton_760.place(x=460,y=110,width=126,height=30)
        GButton_760["command"] = self.GButton_760_command

        GListBox_539=tk.Listbox(root)
        GListBox_539["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_539["font"] = ft
        GListBox_539["fg"] = "#333333"
        GListBox_539["justify"] = "center"
        GListBox_539.place(x=10,y=190,width=570,height=111)

        GButton_902=tk.Button(root)
        GButton_902["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_902["font"] = ft
        GButton_902["fg"] = "#000000"
        GButton_902["justify"] = "center"
        GButton_902["text"] = "Копировать файлы"
        GButton_902.place(x=240,y=10,width=126,height=30)
        GButton_902["command"] = self.GButton_902_command

    def GButton_559_command(self):
        print("command")


    def GButton_995_command(self):
        print("command")


    def GButton_639_command(self):
        print("command")


    def GButton_426_command(self):
        print("command")


    def GButton_306_command(self):
        print("command")


    def GButton_760_command(self):
        print("command")


    def GButton_902_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
