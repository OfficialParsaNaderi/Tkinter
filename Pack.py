from tkinter import HORIZONTAL, Tk ,Scale

root = Tk()

root1 = Scale(master = root , from_ = 0 , to = 42).pack()

root2 = Scale(master = root , from_ =0 , to = 200 , orient = HORIZONTAL).pack()

root.mainloop()