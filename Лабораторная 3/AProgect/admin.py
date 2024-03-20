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
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "

    maxs = 0
    for s in d:
        if len(s)> maxs:
            maxs = len(s)

    matrix.insert (END, " "*maxs)
    al = []
    for i in d:
        for s in d[i]:
            if s in alf and s != " ":
                al.append(s)
    al = sorted(set(al))
    for symb in al:
        matrix.insert(END, symb+" ")

    matrix.insert(END, "\n")
    for users in d:
        matrix.insert(END, users)
        if len(users)< maxs:
            matrix.insert(END, " "*(maxs-len(users)))
        for i in al:
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

#Многопользовательность
def spl_user_addroots(u, r):
    m = get_matrix("matrix.txt")
    if m =='':
        return -1
    d = set_dict(m)
    maxr = ""
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if r == "---":
        for sym in alf:
            f = 0
            for i in d:
                if sym in d[i]:
                    f = 1
            if f == 1:
                maxr+= sym
        r = maxr
        print(r)        
    for us in u.split('-'):
        if not(us in d):
            mb.showerror("Ошибка", "Некорректный пользователь")
            return -1
        if add_roots(us, r)!=0:
            return -1
    return 0
#Добавить права набору юзеров
def add_roots(u_i,r):
    m = get_matrix("matrix.txt")
    d = dict()
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    
    if u_i!= '' and r!='':
        if r != "---":
            for l in r:
                if not(l in(alf)):
                    mb.showerror("Ошибка", "Некорректные права доступа")
                    return -1   
        else:
            d[u_i] = " " 
            mb.showinfo("Info", f"Права пользователей {u} удалены")
        print(u_i)
        for name in u_i:
            if not(name in(alf)):
                mb.showerror("Ошибка", "Некорректное имя")
                return -1
        if m != 0:
            f = open("matrix.txt", 'w')
            d = set_dict(m)
                
            if not u_i in d:
                d[u_i] = set(sorted(r))
            else:
                new_acces = []
                for i in d[u_i]:
                    new_acces.append(i)
                for i in r:
                    if i not in d[u_i]:
                        new_acces.append(i)
                d[u_i] = set(sorted(new_acces))
                
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

#Многопользовательность
def spl_user_create(u, r):
    if r == "---":
        return -1
    if r == "":
        r = " "
    for us in u.split('-'):
        if add_roots(us, r)!=0:
            return -1
    return 0

def spl_user_remroots(u,r):
    for us in u.split('-'):
        if rem_roots(us, r)!=0:
            return -1
    return 0

def rem_roots(u_i,r):
    m = get_matrix("matrix.txt")
    d = dict()
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if u_i!= '' and r!='':
        if r == "---":
            d[u_i] = " " 
            mb.showinfo("Info", f"Права пользователя {u_i} удалены")
        for name in u_i:
            if not(name in(alf)):
                mb.showerror("Ошибка", "Некорректное имя")
                return -1
        if m != 0:
            f = open("matrix.txt", 'w')
            d = set_dict(m)
                
            if not u_i in d:
                mb.showerror("Ошибка", "Такого пользователя нет")
                return -1
            
            new_acces = []
            for i in d[u_i]:
                if i not in r and r != '---':
                    new_acces.append(i)
            
            d[u_i] = set(sorted(new_acces))  
                
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

def changeObj(ob1, ob2):
    m = get_matrix("matrix.txt")
    d = dict()
    d = set_dict(m)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if ob2 not in alf:
        mb.showerror("Ошибка","Недопустимое новое имя объекта")
        return -1
    f=0 
    for user in d:
        if ob2 in d[user]:
            mb.showerror("Ошибка","Имя объекта занято")
            return 0
    
    for user in d:
        s= []
        for i in d[user]:
            if i == ob1:
                s.append(ob2)
            else:
                s.append(i)
        d[user] = s
    f = open("matrix.txt", 'w')
    for users in d:
        f.write(str(users)+"-")
        for i in d[users]:
            f.write(str(i))
        [last] = collections.deque(d, maxlen=1)
        if users != last:
            f.write('\n')
    f.close()
    update()
    return 1

def delObj(ob1):
    m = get_matrix("matrix.txt")
    d = dict()
    d = set_dict(m)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if ob1 not in alf:
        mb.showerror("Ошибка","Недопустимое имя объекта")
        return -1
    for user in d:
        st = []
        for s in d[user]:
            if s != ob1:
                st.append(s)
            d[user] = st

    f = open("matrix.txt", 'w')
    for users in d:
        f.write(str(users)+"-")
        for i in d[users]:
            f.write(str(i))
        [last] = collections.deque(d, maxlen=1)
        if users != last:
            f.write('\n')
    f.close()
    update()
    return 1

def changeSub(ob1, ob2):
    m = get_matrix("matrix.txt")
    d = dict()
    d = set_dict(m)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if not set("<>,\'\":;!_.*-+()/#¤%&?|\)").isdisjoint(ob2):
        mb.showerror("Ошибка", "Некорректное имя пользователя")
        return -1
    f=0 

    if ob2 in d:
        mb.showerror("Ошибка","Имя субъекта занято")
        return 0
    
    if ob1 in d:
        st = d[ob1]
        d.pop(ob1)
        d[ob2] = st
       
    f = open("matrix.txt", 'w')
    for users in d:
        f.write(str(users)+"-")
        for i in d[users]:
            f.write(str(i))
        [last] = collections.deque(d, maxlen=1)
        if users != last:
            f.write('\n')
    f.close()
    update()
    return 1

def delSub(ob1):
    m = get_matrix("matrix.txt")
    d = dict()
    d = set_dict(m)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwz0123456789 "
    if not set("<>,\'\":;!_.*-+()/#¤%&?|\)").isdisjoint(ob1):
        mb.showerror("Ошибка", "Некорректное имя пользователя")
        return -1
    f=0 

    if ob1 not in d:
        mb.showerror("Ошибка","Такого нет")
        return 0
    
    d.pop(ob1)
       
    f = open("matrix.txt", 'w')
    for users in d:
        f.write(str(users)+"-")
        for i in d[users]:
            f.write(str(i))
        [last] = collections.deque(d, maxlen=1)
        if users != last:
            f.write('\n')
    f.close()
    update()
    return 1


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
    grandBtn = tk.Button(text = "GRAND",height=1, width=20, command=lambda: spl_user_addroots(entryLogin.get(), entryRoot.get()))
    grandBtn.grid(row =4, column=1, columnspan= 1, rowspan=1)
    
    createBtn = tk.Button(text = "CREATE",height=1, width=20, command=lambda: spl_user_create(entryLogin.get(), entryRoot.get()))
    createBtn.grid(row =5, column=1, columnspan= 1, rowspan=1)

    addBtn = tk.Button(text = "REMOVE",height=1, width=20, command=lambda: spl_user_remroots(entryLogin.get(), entryRoot.get()))
    addBtn.grid(row =6, column=1, columnspan= 1, rowspan=1)
    #Кнопки редактирования объектов и субъектов
    changeObjBtn = tk.Button(text = "Изменить объект",height=1, width=20, command=lambda: changeObj(entryLogin.get(), entryRoot.get()))
    changeObjBtn.grid(row =7, column=1, columnspan= 1, rowspan=1)

    DelObjBtn = tk.Button(text = "Удалить объект",height=1, width=20, command=lambda: delObj(entryLogin.get()))
    DelObjBtn.grid(row =8, column=1, columnspan= 1, rowspan=1)

    changeSubjBtn = tk.Button(text = "Изменить субъект",height=1, width=20, command=lambda: changeSub(entryLogin.get(), entryRoot.get()))
    changeSubjBtn.grid(row =9, column=1, columnspan= 1, rowspan=1)

    DelSubjBtn = tk.Button(text = "Удалить субъект",height=1, width=20, command=lambda: delSub(entryLogin.get()))
    DelSubjBtn.grid(row =10, column=1, columnspan= 1, rowspan=1)

    tx1 = tk.Label(text="Usernames split -",height=2, width=20)
    tx1.grid(row = 3, column=0 ,rowspan=1,columnspan=1)
    entryLogin = Entry(width = 20)
    entryLogin.grid(row = 4, column=0 ,rowspan=1,columnspan=1)
    tx2 = tk.Label(text="Права",height=2, width=20)
    tx2.grid(row = 3, column=2 ,rowspan=1,columnspan=1)
    entryRoot = Entry(width = 20)
    entryRoot.grid(row =4, column=2,rowspan=1,columnspan=1)

    mainloop()
    

   
            
            
        
    

