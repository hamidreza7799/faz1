import tkinter
from tkinter import ttk
from tkinter import *
import os
from tkinter import messagebox
from tkinter import simpledialog
root=Tk()
#subprocess.Popen("C:/Users/asus/Desktop/New folder (2)/my_image")

#back
class back:
    def __init__(self):
        self.image=PhotoImage(file="back.png")
        self.button=Button(root,image=self.image,command=self.back_f).grid(row=0,padx=5)
        self.label=Label(root,text="back",fg="red").grid(row=2)
        self.path=os.getcwd()
    def back_f(self):
        os.chdir(self.path)
        self.path=os.getcwd()
        s=scrollbar()
        s.creat_files()
        adress.creat()

back=back()       
        
#forward
forward_img=PhotoImage(file="forward.png")
forward_button=Button(root,image=forward_img).grid(row=0,column=1,sticky="w",padx=5)
forward_label=Label(root,text="forward",fg="red").grid(row=2,column=1,sticky="w")
#append
class append:
    def __init__(self):
        self.image=PhotoImage(file="add.png")
        self.button=Button(root,image=self.image,command=self.append_f).grid(row=0,column=2,sticky="e",padx=5)
        self.label=Label(root,text="append",fg="red").grid(row=2,column=2,sticky="e")
        self.entry=ttk.Entry(root)
        self.entry.grid(row=0,column=3,sticky='w')
        self.entry.insert(10,"new_folder")

    def append_f(self):
        try:
            answer = self.entry.get()
            os.mkdir(answer)
            s=scrollbar()
            s.creat_files()
            adress.creat()
        except:
            messagebox.showwarning("Warning","this name was choosed")           
append=append()
#search

#search=Label(root,text='').grid(row=0,column=3,padx=50)
class search:
    def __init__(self):
        self.img=PhotoImage(file="search.png")
        self.button=Button(root,image=self.img,command=self.search_f).grid(row=0,column=4,sticky='e')
        self.entry=ttk.Entry(root)
        self.entry.grid(row=0,column=5,padx=5,sticky='w')
        self.entry.insert(10,"search here")
    
    def search_f(self):
        try:
            answer = self.entry.get()
            (a,b)=os.path.splitext(answer)
            if b=='':
                a=os.path.join(os.getcwd(),str(a))
                os.chdir(str(a))
                s=scrollbar()
                s.creat_files()
                adress.creat()
            else:
                os.system(str(answer))
                adress.creat()
        except:
            messagebox.showwarning("Warning","file not found")
        
search=search()           
#adress
class adress_bar:
    def __init__(self):
        self.window=root
        self.label=Label(self.window,bg='black',fg='white')
        self.label.grid(row=0,column=6)
    def creat(self):
        text=os.getcwd()
        self.label['text']=str(text)
        
adress=adress_bar()
adress.creat()

        
#folde c
def C():
    os.chdir('c:/')
    s=scrollbar()
    s.creat_files()
    adress.creat()
folder_c_img=PhotoImage(file="folder_c.png")
folder_c=Button(root,image=folder_c_img,bg="black",command=C).grid(row=3,column=2,pady=20)
folder_c_label=Label(root,text="Drive_C",fg="red").grid(row=4,column=2)
#folder E
def E():
    os.chdir("E:/")
    s=scrollbar()
    s.creat_files()
    adress.creat()
folder_E_img=PhotoImage(file="folder_c.png")
folder_E=Button(root,image=folder_E_img,bg="black",command=E).grid(row=5,column=2,pady=20)
folder_E_label=Label(root,text="Drive_E",fg="red").grid(row=6,column=2)
#folder D
def D():
    os.chdir("D:/")
    s=scrollbar()
    s.creat_files()
    adress.creat()
folder_D_img=PhotoImage(file="folder_c.png")
folder_D=Button(root,image=folder_D_img,bg="black",command=D).grid(row=7,column=2,pady=20)
folder_D_label=Label(root,text="Drive_D",fg="red").grid(row=8,column=2)
class scrollbar:
    def __init__(self):
        self.window=root
        self.scrollbar=Scrollbar(self.window)
        self.label=Label(self.window).grid(row=3,rowspan=6,column=3,padx=50)
        self.scrollbar.grid(row=3,rowspan=6,column=5,ipady=50,sticky="nw")
        self.listbox=Listbox(self.window,yscrollcommand=self.scrollbar.set)
        self.listbox.grid(row=3,rowspan=6,column=4,ipady=50,sticky="ne")
        self.current_path=os.getcwd()
        self.current_path_list=os.listdir(os.getcwd())
        #creat_files()

    def creat_files(self):
        for file in self.current_path_list:
            self.listbox.insert(END,file)
    
    #self.scrollbar.config(command=listbox.yview)
s=scrollbar()
s.creat_files()
mainloop()
