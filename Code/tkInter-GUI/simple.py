from tkinter import *
from tkinter.ttk import Frame, Button, Style
import subprocess as sub
from tkinter.ttk import Notebook
import shlex
import signal

counter = 0

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.counter = 0

    def test(self):
        print("Tkinter is easy to use!")

    def counter_label(self, label):
        counter = 0
        def count():
            global counter
            counter = counter + 1
            label.config(text=str(counter))
            label.after(1000, count)
        count()

    def addText(self, tab, text):
        tab.insert(END, text)

    def addTest(self, tab):
        tab.insert(END, "Background is running...\n")
        command = 'python "E:\\Huyen Trang\\project\\djangows\\client\\windows\\background_task.py"'
        # tab.insert(END, "Tkinter is easy to use!\n")
        process = sub.call(shlex.split(command))
        print(process)

        tab.insert(END, "Background Task stoped.\n")

        # while 1:
        #     output = process.stdout.readline()
        #     if output == '' and process.poll() is not None:
        #         break
        #     if output:
        #         # print (output.strip())
        #         self.addText(tab, output.strip())
        # rc = process.poll()
        # return rc
    def unix_hard_exit(self):
        os.kill(os.getpid(), signal.SIGKILL)

    def sigint_unix_hard_exit_handler(self, signal, frame):
        self.unix_hard_exit()

    def stopRestore(self, tab):
        tab.insert(END, "Background Task stoped.\n")
        signal.signal(signal.SIGINT, self.sigint_unix_hard_exit_handler)

    def initUI(self):
        self.parent.title("Backup by Ginkgo")
        self.style = Style()
        self.style.theme_use("alt")
        Style().configure("TFrame", background="white")

        # frame = Frame(self, relief=RAISED, borderwidth=0.5)
        # frame.pack(fill=BOTH, expand=True)
        # self.pack(fill=BOTH, expand=True)

        # quitButton = Button(self, text="Quit", command=self.quit)
        # quitButton.pack(side=RIGHT, padx=5, pady=5)

        # bakupButton = Button(self, text="Backup", command=lambda: sub.call('python "E:\\Huyen Trang\\project\\djangows\\client\\windows\\background_task.py"'))
        # bakupButton.pack(side=RIGHT)

        nb = Notebook(root, height=240, width=480)
        tabs = {"Backup": [], "Restore": []}

        for tabname in tabs:
            tab = Text(nb)
            tabs[tabname] = tab
            nb.add(tab, text= tabname)
        nb.pack()

        frame1 = Frame(tabs["Restore"], relief=RAISED, borderwidth=0, height=240, width=580)
        frame1.pack(fill=BOTH, side=BOTTOM, expand=False)

        restoreButton = Button(frame1, text="Restore", command=lambda: self.addTest(tabs["Restore"]))
        restoreButton.pack(side=RIGHT, padx=5, pady=5)
        rStopButton = Button(frame1, text="Stop", command=lambda: self.stopRestore(tabs["Restore"]))
        rStopButton.pack(side=RIGHT, padx=0, pady=0)

        frame2 = Frame(tabs["Backup"], relief=RAISED, borderwidth=0, height=240, width=580)
        frame2.pack(fill=BOTH, side=BOTTOM, expand=False)

        bakupButton = Button(frame2, text="Backup", command=lambda: self.addText(tabs["Backup"]))
        bakupButton.pack(fill=BOTH, side=BOTTOM, padx=0, pady=0)
          
root = Tk() # Create window
#root.geometry("350x200+500+200") # Kích thước window và vị trí hiển thị trên màn hình
app = Example(root) # Tạo một Frame và gắn nó vào window
root.mainloop()
    