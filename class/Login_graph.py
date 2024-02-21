from tkinter import *
import customtkinter as ctk
from Login import * 


class Login_graph(Tk):
    def __init__(self, on_login_success=None):
        super().__init__()
        self.on_login_success = on_login_success

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


        # creation champ email
        self.email = ctk.CTkLabel(self,text= "Email", width=50, height=30,font=('Agency FB', 22, 'bold'), text_color= "white" )
        self.email.place(x=200, y=240, anchor= CENTER)
        self.entry2 = ctk.CTkEntry(self, width=200, height=30, corner_radius= 8, fg_color= "white", text_color="black")
        self.entry2.place(x=200, y= 270, anchor = CENTER)
    
        # creation champ mdp
        self.password = ctk.CTkLabel(self, text="Password", width=50, height=30, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.password.place(x=200, y=310, anchor= CENTER)
        self.entry3 = ctk.CTkEntry(self,show = '*', width= 150, height=30, corner_radius= 8, fg_color="white", text_color="black")
        self.entry3.place(x=200, y=340, anchor = CENTER )

        # Créez un bouton "Afficher"
        self.show_password_button = ctk.CTkButton(self, text="Afficher",width= 30, height=20,corner_radius= 8, command=self.toggle_password_visibility)
        self.show_password_button.place(x=320, y=340, anchor=CENTER)

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
        self.buttonLogin.place(x= 70, y= 450)

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
        self.buttonRegister.place(x= 240, y= 450)

    def toggle_password_visibility(self):
        if self.password_visible:
            self.entry3.configure(show="*")
            self.password_visible = False
        else:
            self.entry3.configure(show="")
            self.password_visible = True

    def verify_login(self):
        # Créez une instance de la classe Login
        login_backend = Login()
    
        #récupérez les valeurs des champs du formulaire
        email = self.entry2.get()
        password = self.entry3.get()
        # Utilisez la méthode login pour vérifier les informations de connexion
        success, user_id = login_backend.login(email, password)
        if success:
            self.destroy()  # ou self.withdraw()
            if self.on_login_success:
                self.on_login_success(user_id)
        else:
            # Gestion de l'échec de la connexion
            print("Login failed. Please check your credentials.")


if __name__ == "__main__":
    login = Login_graph()
    
    login.mainloop()