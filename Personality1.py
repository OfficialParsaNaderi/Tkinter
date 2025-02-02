#Start :

from tkinter import Tk , Entry , Label 

user_question = input(" Do You Want Go To The Personality Tk( Window ) !? \n >>")
if user_question == "yes" or "y" :
    root1 = Tk()
    root1.title( string = " 😎 Personality ! 😉")
    root1["bg"] = "#c3e6e2"
    root1.geometry("700x600")
    root1.iconbitmap("image/icon.ico")

#Label ____________________________________________________________________________________________________________

    root2 = Label ( master = root1 , text = " Enter Your First Name ?! " , font = ("JetBrains Mono" , 10) , 
        bg = "#fcfafa" , fg = "black" , relief = "raised" , border = 20)
    root3 = Label ( master = root1 , text = " Enter Your Last Name ?! " , font = ("JetBrains Mono" , 10) , 
        bg = "#fcfafa" , fg = "black" , relief = "raised" , border = 20)
    root4 = Label ( master = root1 , text = " Enter Your age ?! " , font = ("JetBrains Mono" , 10) , 
        bg = "#fcfafa" , fg = "black" , relief = "raised" , border = 20)
    root5 = Label ( master = root1 , text = " Enter Your Phone Number ?! " , font = ("JetBrains Mono" , 10) ,
        bg = "#fcfafa" , fg = "black" , relief = "raised" , border = 20)
    root6 = Label ( master = root1 , text = " Enter Your Year of Birth ?! " , font = ("JetBrains Mono" , 10) , 
        bg = "#fcfafa" , fg = "black" , relief = "raised" , border = 20)

#Entry ___________________________________________________________________________________________________________

    root7 = Entry ( master = root1 , font = (" " , 10) , width = 15 , bg = "#41f0ed" , relief = "sunken" , border = 20)
    root8 = Entry ( master = root1 , font = (" " , 10) , width = 15 , bg = "#41f0ed" , relief = "sunken" , border = 20)
    root9 = Entry ( master = root1 , font = (" " , 10) , width = 15 , bg = "#41f0ed" , relief = "sunken" , border = 20)
    root10 = Entry ( master = root1 , font = (" " , 10) , width = 15 , bg = "#41f0ed" , relief = "sunken" , border = 20)
    root11 = Entry ( master = root1 , font = (" " , 10) , width = 15 , bg = "#41f0ed" , relief = "sunken" , border = 40)

#grid ____________________________________________________________________________________________________________

    root2.grid( row = 0 , column = 0 , sticky = "nsew" , padx = 20 , pady =20) 
    root7.grid( row = 0 , column = 1 , sticky = "nsew" , padx = 20 , pady =20)

    root3.grid( row = 1 , column = 0 , sticky = "nsew" , padx = 20 , pady =20)
    root8.grid( row = 1 , column = 1 , sticky = "nsew" , padx = 20 , pady =20)

    root4.grid( row = 2 , column = 0 , sticky = "nsew" , padx = 20 , pady =20)
    root9.grid( row = 2 , column = 1 , sticky = "nsew" , padx = 20 , pady =20)

    root5.grid( row = 3, column = 0 , sticky = "nsew" , padx = 20 , pady =20)
    root10.grid( row = 3 , column = 1 , sticky = "nsew" , padx = 20 , pady =20)

    root6.grid( row = 4 , column = 0 , sticky = "nsew" , padx = 20 , pady =20)
    root11.grid( row = 4 , column = 1  , sticky = "nsew" , padx = 20 , pady =20)

#mainloop ____________________________________________________________________________________________________________

    root1.mainloop()

#End.