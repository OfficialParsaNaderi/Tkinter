from tkinter import Tk , Label , PhotoImage , Entry

root1 = Tk ()

image = PhotoImage ()

root1["bg"] = "#caf0f8"
root1.title (string = " 💻🖱️ The First Program of Parsa Naderi  🖌️🎨 ")
root1.geometry("600x200")
root1.iconbitmap ("image/icon.ico")

root2 = Label ( master = root1 , text = " Welcome to the Program Parsa Naderi ! Enter Your Name ? " , bg = "#f05956" ,
fg = "#fcfafa" , font = ("JetBrains Mono" , 10 )) 
root3 = Entry( master = root1 , font = ("" , 10) , width = 15 )

root2.pack ()
root3.pack ()

root1.mainloop ()