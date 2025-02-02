from tkinter import Tk , Label , Entry , Button 

user_question = input(" Do you Want Show The Personality Tk (Window) !? 👍😎❤️ \n ")
if "yes" in user_question or "y" in user_question or "parsa naderi" in user_question or "Parsa Naderi" in user_question:

#def:__________________________________________________________________________________________________________________________________

    def root_manager () :
        f_number = e1.get()
        s_number = e2.get()
        o_action = e3.get()

        if o_action == "+" :
            r_number = int(f_number) + int(s_number)
            print(f" result : {r_number} ❤️")
        elif o_action == "-" :
            r_number = int(f_number) - int(s_number)
            print(f" result : {r_number} ❤️")
        elif o_action == "*" :
            r_number = int(f_number) * int(s_number)
            print(f" result : {r_number} ❤️")
        elif o_action == "/" :
            r_number = int(f_number) / int(s_number)
            print(f" result : {r_number} ❤️")
        elif o_action == "**" :
            r_number = int(f_number) ** int(s_number)
            print(f" result : {r_number} ❤️")
        elif o_action == "//" :
            r_number = int(f_number) // int(s_number)
            print(f" result : {r_number} ❤️")
        else :
            print(f" sorry {user_question} I don't Do Any Work For You ! 👍😢 ")

        file_info = open("UserInfo.txt" , "a")
        file_info.write(f"First Number : {f_number}\nSecond Number : {s_number}\n")
        file_info.close()

#cnf:__________________________________________________________________________________________________________________________________

    configurations = {
        "label" : {
            "bg" : "#c3e6e2" ,
            "fg" : "black" ,
            "font" : ("JetBrains Mono" , 16 ) ,
            "relief" : "raised" ,
            "border" : 20 ,
            "justify" : "center" ,
        } ,
        "entry" : {
            "bg" : "#c3e6e2" ,
            "fg" : "black" ,
            "font" : ("JetBrains Mono" , 16 ) ,
            "relief" : "raised" ,
            "border" : 5 ,
            "justify" : "center" ,
        } ,
        "button" : {
            "bg" : "#fcfcfa" ,
            "fg" : "white" ,
            "font" : ("JetBrains Mono" , 16 ) ,
            "relief" : "raised" ,
            "border" : 20 ,
        }
    }

#Tk:__________________________________________________________________________________________________________________________________

    root1 = Tk()
    root1.title("😎 Personality ! ❤️")
    root1["bg"] = "#41f0ed"
    root1.geometry("1400x1200")

#Label:__________________________________________________________________________________________________________________________________

    l1 = Label ( master = root1 , text = " What is Your Favorite Number (1) ! 🧮 " , cnf = configurations["label"])

    l2 = Label ( master = root1 , text = " What is your Favorite Number (2) ! 🧮 " , cnf = configurations["label"])

    l3 = Label ( master = root1 , text = " What is Your Favorite Operators !  🧮 " , cnf = configurations["label"])

#Entry:__________________________________________________________________________________________________________________________________

    e1 = Entry ( master = root1 , cnf = configurations["entry"] )

    e2 = Entry ( master = root1 , cnf = configurations["entry"] )

    e3 = Entry ( master = root1 , cnf = configurations["entry"] )

#Button:__________________________________________________________________________________________________________________________________

    button = Button (master = root1 , text = " press to show result ! " , cnf = configurations["button"] , command = root_manager)

#grid:__________________________________________________________________________________________________________________________________

    l1.grid( row = 1 , column = 0 , sticky = "nsew" , padx = 20 , pady = 20 )
    e1.grid( row = 2 , column = 0 , sticky = "nsew" , padx = 20 , pady = 20 )

    l2.grid( row = 1 , column = 1 , sticky = "nsew" , padx = 20 , pady = 20 )
    e2.grid( row = 2 , column = 1 , sticky = "nsew" , padx = 20 , pady = 20 )

    l3.grid( row = 1 , column = 3 , sticky = "nsew" , padx = 20 , pady = 20 )
    e3.grid( row = 2 , column = 3 , sticky = "nsew" , padx = 20 , pady = 20 )

    button.grid( row = 4 , column = 1 , columnspan = 2 , sticky = "nsew" , padx = 20 , pady = 20 )

#mainloop:__________________________________________________________________________________________________________________________________

    root1.mainloop()