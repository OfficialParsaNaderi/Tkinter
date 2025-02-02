from tkinter import W , Canvas, IntVar , Tk , Checkbutton

root = Tk()

root1 = IntVar()

Checkbutton(master = root , text = " man " , variable = root1 ).grid(row = 0 , sticky = W)

root2 = IntVar()

Checkbutton(master = root , text = " Woman " , variable = root2).grid(row = 1 , sticky = W)

root.mainloop()