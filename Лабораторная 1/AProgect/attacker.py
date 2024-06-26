import os
import shutil
from tkinter import *
from tkinter import ttk

save_stream = open("../Intruder/save.txt", "r")
numberfile =int(save_stream.read())
save_stream.close()


init_scanning = False
def copying(diff_list):
    
    for file in diff_list:
        buffer = ""
        copy_stream = open("../Public/"+str(file), "r")
        buff = copy_stream.read()
        create_stream = open("../Intruder/"+str(file), "w")
        create_stream.write(buff)
        copy_stream.close()
        create_stream.close()

def udpate_files(pub_list, int_list):
    global numberfile
    for p in pub_list:
        for i in int_list:
            buf_p = ""
            buf_i = ""
            if p == i:
                p_stream = open("../Public/"+p, "r")
                buf_p = p_stream.read()
                i_stream = open("../Intruder/"+i, "r")
                buf_i = i_stream.read()
                if buf_p != buf_i:
                    flag = 0
                    for k in int_list:
                        p_stream = open("../Public/"+p, "r")
                        buf_p = p_stream.read()
                        i_stream = open("../Intruder/"+k, "r")
                        buf_i = i_stream.read()
                        if buf_i == buf_p:
                            flag = 1
                    if flag == 0:    
                        shutil.copy("..//Public//"+p,"..//Intruder//"+str(numberfile)+"-"+p)
                        numberfile += 1
                        save_stream = open("../Intruder/save.txt", "w+")
                        save_stream.write(str(numberfile))
                        save_stream.close()


def timed_checker(status=None):
    global init_scanning


    if status == "start":
        init_scanning = True
        st_but["text"] = "Сканнер\nзапущен"
    if status == "stop":
        init_scanning = False
        st_but["text"] = "Запустить\n сканнер"
    if init_scanning == True:
        pub_list = os.listdir("../Public")
        int_list = os.listdir("../Intruder")
        pub_list_set=set(pub_list)
        int_list_set=set(int_list)
    
        diff = pub_list_set.difference(int_list_set)
        diff_list = list(diff)
        copying(diff_list)
        udpate_files(pub_list, int_list)
        # for file in diff_list:
        #     shutil.copy("..//Public//"+file, "..//Intruder")
        public_listbox.after(1000, timed_checker)
    return 0


# def move_all():
#     shutil.copytree("Public", "Intruder", dirs_exist_ok = True)
#     return 0

def update_file_list(listbox, directory_path):
    file_list = os.listdir(directory_path)
    listbox.delete(0, END)
    for file in file_list:  
        listbox.insert(END, file)
    window.after(1000, update_file_list, listbox, directory_path)  # Проверяем каждую секунду

if __name__ == '__main__':
    
    window = Tk()  
    window.title("Attacker's window")  
    window.geometry('700x300')
    window.configure(bg='#4B0082')
    window.iconphoto(False, PhotoImage(file="anon.png"))
    window.resizable(width=False, height=False)

    for i in range(3): window.columnconfigure(index=i, weight=1)
    for i in range(8): window.rowconfigure(index=i, weight=1)

    label_public = Label(text = "Публичная папка",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_public.grid(row=0, column=0)
    label_button = Label(text = "Выберете действие",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_button.grid(row=1, column=1)
    label_intr = Label(text = "Папка злоумышленника",background="#000000", foreground="#00FF7F",font=("Arial", 14),relief="ridge")
    label_intr.grid(row=0, column=2)
    
    public_listbox = Listbox(yscrollcommand=True)
    public_listbox.grid(row=1, column=0, rowspan=6)
    intr_listbox = Listbox(yscrollcommand=True)
    intr_listbox.grid(row=1, column=2, rowspan=6)
    update_file_list(public_listbox, "../Public")
    update_file_list(intr_listbox, "../Intruder")

    #ttk.Button(text="Перенести\n      все",command =move_all).grid(row=2, column=1, padx=2, pady=2)

    st_but = ttk.Button(text="Запустить\n сканнер",\
               command =lambda: timed_checker("start"))
    st_but.grid(row=3, column=1, padx=2, pady=2)
    ttk.Button(text="Остановить\n  сканнер",\
               command =lambda: timed_checker("stop")).grid(row=4, column=1, padx=2, pady=2)
    

    mainloop()
    

   
            
            
        
    

