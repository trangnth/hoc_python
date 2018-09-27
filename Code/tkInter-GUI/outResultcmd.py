from tkinter import *
from tkinter.ttk import Notebook
import subprocess as sub

def addText(tab):
    tab.insert(END, sub.Popen('python "C:\\Users\\Bosua\\Desktop\\cmd.py"', stdout=sub.PIPE, stderr=sub.PIPE).communicate()[0])

root = Tk()

nb = Notebook(root, height=240, width=480)
tabs = {"foo": [], "bara": []}

for tabname in tabs:
    tab = Text(nb)
    tabs[tabname] = tab
    nb.add(tab, text= tabname)
nb.pack()

# Button(root, text= "Add text!", command = lambda: addText(tabs["foo"])).pack()
quitButton = Button(root, text="Quit", command=root.quit)
quitButton.pack(side=RIGHT, padx=5, pady=5)

bakupButton = Button(root, text="Backup", command=lambda: addText(tabs["foo"]))
bakupButton.pack(side=RIGHT)


root.mainloop()