import os
import shutil
from tkinter import *
import tkinter as tk
import collections
import tkinter.messagebox as mb

def get_matrix(path):
    f = open(path)
    buf = f.read()
    m = 0
    if buf!= "" and '\n' in buf:
        m = buf.split('\n')
    f.close()
    return m

def print_matrix(d):
    matrix.delete("1.0", END)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789"
    maxs = 0
    for s in d:
        if len(s)> maxs:
            maxs = len(s)

    matrix.insert (END, " "*maxs)
    for symb in alf:
        matrix.insert(END, symb+" ")
    matrix.insert(END, "\n")
    for users in d:
        matrix.insert(END, users)
        if len(users)< maxs:
            matrix.insert(END, " "*(maxs-len(users)))
        for i in alf:
            if i in d[users]:
                matrix.insert(END, "+ ")
            else:
                matrix.insert(END, "- ")
        matrix.insert(END, "\n")
            
def set_dict(m):
    d = dict()
    for s in m:
        a, b = s.split("-")
        d[a] = sorted(set(b))
    return d

def update():
    m = get_matrix("matrix.txt")
    if m != 0:
        d = set_dict(m)
        print_matrix(d)
    return 0

def change_roots(u,r):
    m = get_matrix("matrix.txt")
    d = dict()
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789"
    if u!='' and r!='':
        if r != "---":
            for l in r:
                if not(l in(alf)):
                    mb.showerror("Ошибка", "Некорректные права доступа")
                    return -1   
        for name in u:
            if not(name in(alf)):
                mb.showerror("Ошибка", "Некорректное имя")
                return -1
        if m != 0:
            f = open("matrix.txt", 'w')
            d = set_dict(m)
            print(d)
            d[u] = set(sorted(r))
            if r == "---":
                d.pop(u)
                mb.showinfo("Info", f"Пользователь {u} удален")
            for users in d:
                f.write(str(users)+"-")
                for i in d[users]:
                    f.write(str(i))
                [last] = collections.deque(d, maxlen=1)
                if users != last:
                    f.write('\n')
            f.close()
            update()
        else:
            return -1
    else:
        mb.showerror("Ошибка", "Некорректные данные")
        return -1
    return 0
if __name__ == '__main__':
    
    window = Tk()  
    window.title("Admin's window")  
    window.geometry('600x500')
    window.configure(bg='#2B2381')
    window.resizable(width=False, height=False)

    for i in range(3): window.columnconfigure(index=i, weight=1)
    for i in range(15): window.rowconfigure(index=i, weight=1)

    txt_frm = tk.Frame(window, width=150, height=150)
    txt_frm.grid(row=1, column=0, rowspan= 1, columnspan=3)
    
    mat_text = tk.Label(text="Матрица доступов",height=2, width=30)
    mat_text.grid(row = 0, column=1, columnspan= 1, rowspan=1)

    matrix = tk.Text(txt_frm, borderwidth=3, relief="sunken",height=10, width=60)
    matrix.config(font=("consolas", 12), undo=True, wrap=NONE)
    matrix.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)

    scrollb = tk.Scrollbar(txt_frm,orient=HORIZONTAL, command=matrix.xview)
    scrollb.grid(row=1, column=0, sticky='nsew')
    matrix['xscrollcommand'] = scrollb.set

    scrollby = tk.Scrollbar(txt_frm, orient=VERTICAL, command=matrix.yview)
    scrollby.grid(row=0, column=1, sticky='nsew')
    matrix['yscrollcommand'] = scrollby.set    

    update()
    addBtn = tk.Button(text = "Изменить права",height=1, width=20, command=lambda: change_roots(entryLogin.get(), entryRoot.get()))
    addBtn.grid(row =4, column=1, columnspan= 1, rowspan=1)

    tx1 = tk.Label(text="Имя пользователя",height=2, width=20)
    tx1.grid(row = 3, column=0 ,rowspan=1,columnspan=1)
    entryLogin = Entry(width = 20)
    entryLogin.grid(row = 4, column=0 ,rowspan=1,columnspan=1)
    tx2 = tk.Label(text="Новые права \n(для удаления введите ---)",height=2, width=20)
    tx2.grid(row = 3, column=2 ,rowspan=1,columnspan=1)
    entryRoot = Entry(width = 20)
    entryRoot.grid(row =4, column=2,rowspan=1,columnspan=1)

    mainloop()
    

   
            
            
        
    

