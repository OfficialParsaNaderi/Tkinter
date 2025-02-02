from tkinter import IntVar , Tk , Radiobutton, Variable

root = Tk()

root1 = IntVar()

Radiobutton(master = root , text = " Chat GPT ", variable = root1 , value = 1).pack()

Radiobutton(master = root , text = " BING ", variable = root1 , value = 2).pack()

root.mainloop()