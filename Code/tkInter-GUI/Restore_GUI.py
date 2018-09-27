from tkinter import *
from tkinter import messagebox
import subprocess as sub
import shlex
from tkinter.ttk import Notebook


def backup():
	path = "E:\\Huyen Trang\\project\\djangows\\client\\windows\\backcli.py"
	command = "python \"" + path + "\" -t " + file_name.get() + " -s " + server_name.get()
	process = sub.Popen(shlex.split(command), stdout=sub.PIPE, stderr=sub.PIPE).communicate()

	list1.insert(END, process[0])
	list1.insert(END, process[1])


def restore():
	pass


def listcli():
	pass


window = Tk()

window.title("Backup by Ginkgo")

# def on_closing():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         window.destroy()

# window.protocol("WM_DELETE_WINDOW", on_closing)  # handle window closing

nb = Notebook(window)

tabs = {"Backup": [], "Restore": []}
for tabname in tabs:
    tab = Frame(nb)
    tabs[tabname] = tab
    nb.add(tab, text= tabname)
nb.pack()


# Backup tab
l1=Label(tabs["Backup"], text="Backup File")
l1.grid(row = 0, column = 0, columnspan=2)

l2=Label(tabs["Backup"], text="Files")
l2.grid(row = 1, column = 1)

l3=Label(tabs["Backup"], text="Server")
l3.grid(row = 2, column = 1)

l4=Label(tabs["Backup"], text="G:\\\\test.txt")
l4.grid(row = 1, column = 3, padx=5)

l5=Label(tabs["Backup"], text="192.168.20.51")
l5.grid(row = 2, column = 3, padx=5)

l6=Label(tabs["Backup"], text="Output")
l6.grid(row = 3, column = 1)


file_name=StringVar()
e1=Entry(tabs["Backup"], textvariable=file_name, width=30)
e1.grid(row=1, column=2, padx=2, pady=2)

server_name=StringVar()
e1=Entry(tabs["Backup"], textvariable=server_name, width=30)
e1.grid(row=2, column=2, padx=2, pady=2)

#define Listbox
#list1=Text(window, height=6, width=41, wrap=WORD)
list1=Text(tabs["Backup"], height=10, width=35, wrap=NONE)
list1.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Atach Scrollbar to the list
sb1=Scrollbar(tabs["Backup"])
sb1.grid(row=3, column=4, padx=5, sticky=N+S)

sb2=Scrollbar(tabs["Backup"], orient=HORIZONTAL)
sb2.grid(row=4, column=2, columnspan=2, sticky=E+W)

#Apply to the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.configure(xscrollcommand=sb2.set)
sb2.configure(command=list1.xview)


b1=Button(tabs["Backup"], text="Backup", width=12, command=backup)
b1.grid(row=5, column=2, padx=5, pady=5, columnspan=2)


# Restore tab
R1=Label(tabs["Restore"], text="Restore File      ")
R1.grid(row = 0, column = 0, columnspan=2)

R2=Label(tabs["Restore"], text="Files")
R2.grid(row = 1, column = 1)

R3=Label(tabs["Restore"], text="Backup ID")
R3.grid(row = 2, column = 1)

R5=Label(tabs["Restore"], text="List Version")
R5.grid(row = 3, column = 1)

R6=Label(tabs["Restore"], text="G:\\\\test.txt")
R6.grid(row = 1, column = 3)

R7=Label(tabs["Restore"], text="13")
R7.grid(row = 2, column = 3)

restore_file=StringVar()
r1=Entry(tabs["Restore"], textvariable=restore_file, width=30)
r1.grid(row=1, column=2, padx=2, pady=2)

backup_id=StringVar()
r1=Entry(tabs["Restore"], textvariable=backup_id, width=30)
r1.grid(row=2, column=2, padx=2, pady=2)


list2=Text(tabs["Restore"], height=10, width=30, wrap=NONE)
list2.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

# Atach Scrollbar to the list
sr1=Scrollbar(tabs["Restore"])
sr1.grid(row=3, column=4, padx=5, sticky=N+S)

sr2=Scrollbar(tabs["Restore"], orient=HORIZONTAL)
sr2.grid(row=4, column=2, columnspan=2, sticky=E+W)

#Apply to the list
list2.configure(yscrollcommand=sr1.set)
sr1.configure(command=list2.yview)

list2.configure(xscrollcommand=sr2.set)
sr2.configure(command=list2.xview)

p1=Button(tabs["Restore"], text="Restore", width=12, command=restore)
p1.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

p2=Button(tabs["Restore"], text="List", command=listcli)
p2.grid(row=3, column=5, padx=5, pady=5)


#window.geometry("350x200+500+200")
window.mainloop()