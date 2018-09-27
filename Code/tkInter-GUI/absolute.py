from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style
 
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
  
    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("C:\\Users\\Bosua\\Desktop\\Vai Thu\\Intern\\Timhieu_Docker\\img\\docker-3.png") #Tạo đối tượng ảnh
        bardejov = ImageTk.PhotoImage(bard)         # Gán chúng vào chương trình
        label1 = Label(self, image=bardejov)        # sử dụng class Label để hiển thị chữ và ảnh
        label1.image = bardejov
        label1.place(x=10, y=10)

        rot = Image.open("C:\\Users\\Bosua\\Desktop\\Vai Thu\\Intern\\Timhieu_Docker\\img\\1.png")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=200, y=400)

        minc = Image.open("C:\\Users\\Bosua\\Desktop\\Vai Thu\\Intern\\Timhieu_Docker\\img\\2.png")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=900, y=50)
  
root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()