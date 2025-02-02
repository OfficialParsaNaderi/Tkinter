from tkinter import Listbox , Tk

root = Tk()

lb = Listbox(root)
lb.insert(1, "python")
lb.insert(2, "Java")
lb.insert(3, "C++")
lb.insert(4, "Any others")
lb.pack()

root.mainloop()