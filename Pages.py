from tkinter import Tk , Label , Button

root = Tk()
root.geometry("400x300")
root.title(" Python Programm !")
root["bg"] = "#fcfafa"

f = [ "Times bold" , 15]

def nextPage() :
    root.destroy()

def prevPage() :
    root.destroy()

Label (
    root , text = " This is First Page " , padx = 20 , pady = 20 ,
    bg = "#5d8" , font = f
).pack(expand = True , fill = "both")

Button (
    root , text = " Previous Page " , font = f , command = nextPage
).pack(fill ="x" , expand = True , side = "left")

Button (
    root , text = " NextPage " , font = f , command = prevPage 
).pack(fill = "x" , expand = True , side = "left")

root.mainloop()