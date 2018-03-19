from tkinter import *
from tkinter import ttk

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
   e1.delete(0,END)
   e2.delete(0,END)

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = ttk.Entry(master)
e2 = ttk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e1.insert(5,"Miller")
e2.insert(10,"Jill")
Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
class append:
    def __init__(self):
        self.image=PhotoImage(file="add.png")
        self.button=Button(master,image=self.image,command=self.append_f).grid(row=0,column=2,sticky="e",padx=5)
        self.label=Label(master,text="append",fg="red").grid(row=2,column=2,sticky="e")


    def append_f(self):
        try:
            answer = simpledialog.askstring("Input", "choose a name",parent=master)
            os.mkdir(answer)
            s=scrollbar()
            s.creat_files()
        except:
            messagebox.showwarning("Warning","this name was choosed")
            
append=append()
entry=ttk.Entry(master)
entry.grid(row=0,column=3,sticky="w")
entry.insert(10,'s')
mainloop( )
