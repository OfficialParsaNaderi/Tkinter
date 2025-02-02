from tkinter import Tk , Menu 

root = Tk()
menu = Menu(root)

root.config(menu = menu)
file_menu = Menu(menu)

menu.add_cascade(label="file",menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="open...")

file_menu.add_separator()

file_menu.add_command(label="Exit",command=root.quit)
help_menu = Menu(menu)
menu.add_cascade(label="Help",menu=help_menu)
help_menu.add_command(label="About")

root.mainloop()