# Start :
from tkinter import Tk , PhotoImage , Label , Entry , mainloop

user_question = str(input(" Do You Want Open The Personal Tk( Window ) 😎❤️ ?! \n >>"))
if user_question == "yes" or "y" :

    # root1 :
    def root1 () :
        root1 = Tk()

        root1.title( string = " 👧🏿 First Name ! 👦🏻 ")
        root1.geometry("600x200")
        root1.iconbitmap("image/icon.ico")
        root1 ["bg"] = "#1ef3fa"

        root_label = Label ( master = root1 , text = "  What's Your First Name ?! " , bg = "#fa1e34" , 
        fg = "#fcfafa" , font = ("JetBrains Mono " , 10))

        root_Entry = Entry ( master = root1 , font = (" " , 10) , width = 5)

        root_label.pack()
        root_Entry.pack()

        root1.mainloop()

    root1()

    # root2 : 
    def root2 () :
        root2 = Tk()

        root2.title( string = " 👦🏻 Last Name  ! 👧🏿")
        root2.geometry("600x200")
        root2.iconbitmap("image/icon.ico")
        root2["bg"] = "#eff230"

        root_label = Label ( master = root2 , text = " What's Your Last Name ?! " , bg = "#48f756" ,
        fg = "#fcfafa" , font = ("JetBrains Mono" , 10))

        root_Entry = Entry ( master = root2 , font = (" ", 10) , width = 5)

        root_label.pack()
        root_Entry.pack()

        root2.mainloop()

    root2()

    # root3 :
    def root3 () :
        root3 = Tk()

        root3.title( string = " 👧🏿 Age ! 👦🏻")
        root3.geometry("600x200")
        root3.iconbitmap("image/icon.ico")
        root3["bg"] = "#f7a0fa"

        root_label = Label ( master = root3 , text = " How Old are You ?! " , bg = "#8ca7ed" , 
        fg = "#fcfafa" , font = ("JetBrains Mono" , 10))

        root_Entry = Entry ( master = root3 , font = (" ", 10) , width = 5)

        root_label.pack()
        root_Entry.pack()

        root3.mainloop()

    root3()
# End .