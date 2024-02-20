from tkinter import *
import customtkinter as ctk
from Login import * 
from MainPage_graph import *


class Login_graph(Tk):
    def __init__(self):
        super().__init__()

        # creation de la fenetre
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

        # # creation champ pour le prenom
        # self.firstname = ctk.CTkLabel(self, text= "Firstname", width=50, height= 20, font=('Agency FB', 22, 'bold'), text_color="white")
        # self.firstname.place(x=200, y=220, anchor= CENTER )
        # self.entry = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        # self.entry.place(x= 200, y =250, anchor = CENTER )

        # # creation champ nom 
        # self.surname = ctk.CTkLabel(self, text= "Surname", width=50, height=20, font=('Agency FB', 22, 'bold'), text_color= "white")
        # self.surname.place(x= 200, y= 280, anchor = CENTER)
        # self.entry1 = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        # self.entry1.place(x=200, y= 310, anchor = CENTER)

        # creation champ email
        self.email = ctk.CTkLabel(self,text= "Email", width=50, height=30,font=('Agency FB', 22, 'bold'), text_color= "white" )
        self.email.place(x=200, y=340, anchor= CENTER)
        self.entry2 = ctk.CTkEntry(self, width=200, height=30, corner_radius= 8, fg_color= "white", text_color= "black")
        self.entry2.place(x=200, y= 370, anchor = CENTER)
    
        # creation champ mdp
        self.password = ctk.CTkLabel(self, text="Password", width=50, height=30, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.password.place(x=200, y=400, anchor= CENTER)
        self.entry3 = ctk.CTkEntry(self,show = '*', width= 150, height=30, corner_radius= 8, fg_color="white")
        self.entry3.place(x=200, y=430, anchor = CENTER )

        # Créez un bouton "Afficher"
        self.show_password_button = ctk.CTkButton(self, text="Afficher",width= 30, height=20,corner_radius= 8, command=self.toggle_password_visibility)
        self.show_password_button.place(x=320, y=430, anchor=CENTER)

        # Gardez une variable pour suivre l'état actuel du mot de passe (masqué ou affiché)
        self.password_visible = False

        #creation bouton connexion
        self.buttonLogin = ctk.CTkButton(self, 
                                         text="LOGIN", 
                                         width=80, 
                                         height=20,
                                         corner_radius= 10,
                                         font=("Agency FB", 21, "bold"),
                                         border_width= 2,
                                         border_color= "white",
                                         fg_color="#e74353",
                                         hover_color="#ef511c",
                                         command= self.verify_login 
                                         )
        self.buttonLogin.place(x= 70, y= 500)

        # creation bouton inscription
        self.buttonRegister = ctk.CTkButton(self, 
                                            text="REGISTER",
                                            width=80, 
                                            height=20,
                                            corner_radius= 10,
                                            font=("Agency FB", 21, "bold"),
                                            border_width= 2,
                                            border_color= "white",
                                            fg_color="#e74353",
                                            hover_color="#ef511c", 
                                            command= self.go_register
                                            )
        self.buttonRegister.place(x= 240, y= 500)

    def toggle_password_visibility(self):
        if self.password_visible:
            self.entry3.configure(show="*")
            self.password_visible = False
        else:
            self.entry3.configure(show="")
            self.password_visible = True

    def verify_login(self):
        # Créez une instance de la classe Login (backend)
        login_backend = Login()
        
        # Récupérez les valeurs des champs du formulaire
        
        email = self.entry2.get()
        password = self.entry3.get()

        # Appelez la méthode login du backend pour vérifier les informations d'identification
        success, user_id = login_backend.login( email, password)

        # Si la connexion est réussie (success est True), affichez la page principale
        if success:
            print("Welcome")
            # Fermez la fenêtre de connexion
            self.destroy()
            # Affichez la page principale
            goMainpage = MainPage_graph()
            goMainpage.mainloop()
        else:
            print("Login failed. Please check your credentials.")

    def go_register(self):
        self.destroy()
        register = Register_graph()
        register.mainloop()


if __name__ == "__main__":
    login = Login_graph()
    
    login.mainloop()
        


