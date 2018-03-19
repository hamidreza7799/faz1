import tkinter
from tkinter import ttk
from tkinter import *
import os
from tkinter import messagebox
from tkinter import simpledialog
root=Tk()
#subprocess.Popen("C:/Users/asus/Desktop/New folder (2)/my_image")
#menu
def hello():
    print ("hello!")
def open_f():
    answer = simpledialog.askstring("Input", "please enter your file's name",parent=root)
    try:
        
        (a,b)=os.path.splitext(answer)
        if b=='':
            a=os.path.join(os.getcwd(),str(a))
            back.save_path()
            os.chdir(str(a))
            back.save_path()
            s=scrollbar()
            s.creat_files()
            adress.creat()
        else:
            back.save_path()
            os.system(str(answer))
            back.save_path()
            adress.creat()
    except:
        messagebox.showwarning("Warning","file not found")
    
    

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_f)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)
# display the menu
root.config(menu=menubar)

#back
class back:
    def __init__(self):
        self.image=PhotoImage(file="back.png")
        self.button=Button(root,image=self.image,command=self.back_f).grid(row=0,padx=5)
        self.label=Label(root,text="back",fg="red").grid(row=2)
        self.path_list=[os.getcwd()]

    def save_path(self):
        path=os.getcwd()
        if len(self.path_list)==0:
            self.path_list+=[path]
        elif self.path_list[len(self.path_list)-1]!=path:
            self.path_list+=[path]
    def back_f(self):
        if len(self.path_list)>0:
            os.chdir(self.path_list[len(self.path_list)-1])
            
            self.path_list.remove(self.path_list[len(self.path_list)-1])
            s=scrollbar()
            s.creat_files()
            adress.creat()
        else:
            jsfjgsvfou=1
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
                back.save_path()
                os.chdir(str(a))
                back.save_path()
                s=scrollbar()
                s.creat_files()
                adress.creat()
            else:
                back.save_path()
                os.system(str(answer))
                back.save_path()
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
    back.save_path()
    os.chdir('c:/')
    back.save_path()
    s=scrollbar()
    s.creat_files()
    adress.creat()
folder_c_img=PhotoImage(file="folder_c.png")
folder_c=Button(root,image=folder_c_img,bg="black",command=C).grid(row=3,column=2,pady=20)
folder_c_label=Label(root,text="Drive_C",fg="red").grid(row=4,column=2)
#folder E
def E():
    try:
        back.save_path()
        os.chdir("E:/")
        back.save_path()
        s=scrollbar()
        s.creat_files()
        adress.creat()
    except:
        messagebox.showwarning("Warning","file not found")
        
folder_E_img=PhotoImage(file="folder_c.png")
folder_E=Button(root,image=folder_E_img,bg="black",command=E).grid(row=5,column=2,pady=20)
folder_E_label=Label(root,text="Drive_E",fg="red").grid(row=6,column=2)
#folder D
def D():
    back.save_path()
    os.chdir("D:/")
    back.save_path()
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
