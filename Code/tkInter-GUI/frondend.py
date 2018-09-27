from tkinter import *

window = Tk()

l1=Label(window, text="Title")
l1.grid(row = 0, column = 0)

l2=Label(window, text="Author")
l2.grid(row = 0, column = 2)

l1=Label(window, text="Year")
l1.grid(row = 1, column = 0)

l1=Label(window, text="ISMN")
l1.grid(row = 1, column = 2)

#define Entries
title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)


author_text=StringVar()
e1=Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text=StringVar()
e1=Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

isbn_text=StringVar()
e1=Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)

#define Listbox
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, padx=5, pady=5)

# Atach Scrollbar to the list
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#Apply to the list
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


#define buttons
b1=Button(window, text="View All", width=12)
b1.grid(row=2, column=3, padx=2, pady=2)

b2=Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3, padx=2, pady=2)

b4=Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b1=Button(window, text="Delete", width=12)
b1.grid(row=6, column=3, padx=2, pady=2)

b1=Button(window, text="Close", width=12)
b1.grid(row=7, column=3, padx=1, pady=2)

window.mainloop()
