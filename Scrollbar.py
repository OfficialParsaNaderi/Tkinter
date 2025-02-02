from tkinter import BOTH, END, LEFT, Y, Listbox , Tk , Scrollbar , RIGHT

root = Tk()

Scrollbar = Scrollbar(root)
Scrollbar.pack(side = RIGHT , fill = Y)
list = Listbox(master = root , yscrollcommand = Scrollbar.set )
for line in range(100) :
    list.insert(END , "This is line Number ! " + str(line))
list.pack(side = LEFT , fill = BOTH )
Scrollbar.config( command = list.yview )

root.mainloop()