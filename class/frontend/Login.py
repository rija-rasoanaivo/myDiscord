from tkinter import *
import customtkinter as ctk

class Loginpage(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x650")
        self.title("Login Page") 
        self.configure(bg = "#c3caf7")
        self.frame = ctk.CTkFrame(self,width= 150,height= 150)
        self.frame.place( x= 200, y=70, anchor = CENTER)

        # telecharger le logo 
        self.logo = PhotoImage(file="image/logo/logoJRM1.png" )

        # Ajouter le logo à un widget Label dans le cadre
        self.logo_label = Label(self.frame, image=self.logo, bg='#c3caf7')  
        self.logo_label.pack(side=TOP)

        # titre de la page
        self.label = ctk.CTkLabel(self, text= "LOGIN", width= 50, height=50,font=('Broadway', 25), text_color="white" )
        self.label.place(x= 200, y=160, anchor = CENTER)

        # creation champ pour le prenom
        self.firstname = ctk.CTkLabel(self, text= "Firstname", width=50, height= 20, font=('Agency FB', 22, 'bold'), text_color="white")
        self.firstname.place(x=200, y=220, anchor= CENTER )
        entry = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        entry.place(x= 200, y =250, anchor = CENTER )

        # creation champ nom 
        self.surname = ctk.CTkLabel(self, text= "Surname", width=50, height=20, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.surname.place(x= 200, y= 280, anchor = CENTER)
        entry1 = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        entry1.place(x=200, y= 310, anchor = CENTER)

        # creation champ email
        self.email = ctk.CTkLabel(self,text= "Email", width=50, height=30,font=('Agency FB', 22, 'bold'), text_color= "white" )
        self.email.place(x=200, y=340, anchor= CENTER)
        entry2 = ctk.CTkEntry(self, width=200, height=30, corner_radius= 8, fg_color= "white")
        entry2.place(x=200, y= 370, anchor = CENTER)

    
        # creation champ mdp
        self.password = ctk.CTkLabel(self, text="Password", width=50, height=30, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.password.place(x=200, y=400, anchor= CENTER)
        entry3 = ctk.CTkEntry(self, width= 150, height=30, corner_radius= 8, fg_color="white")
        entry3.place(x=200, y=430, anchor = CENTER )

    
    def buttonLogin(self):
        #creation bouton connexion
        self.buttonLogin = ctk.CTkButton(self, 
                                         text="LOGIN", 
                                         width=80, 
                                         height=20,
                                         corner_radius= 5,
                                         font=("Agency FB", 21, "bold"),
                                         border_width= 2,
                                         border_color= "white",
                                         fg_color="#e74353",
                                         hover_color="#ef511c",
                                         command= "welcome"
                                         )
        self.buttonLogin.place(x= 70, y= 500)

    def buttonRegister(self):
        # creation bouton inscription
        self.buttonRegister = ctk.CTkButton(self, 
                                            text="REGISTER",
                                            width=80, 
                                            height=20,
                                            corner_radius= 5,
                                            font=("Agency FB", 21, "bold"),
                                            border_width= 2,
                                            border_color= "white",
                                            fg_color="#e74353",
                                            hover_color="#ef511c", 
                                            command= "register")
        self.buttonRegister.place(x= 240, y= 500)
        

test = Loginpage()
test.buttonLogin()
test.buttonRegister()
test.mainloop()
        


