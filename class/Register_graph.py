from tkinter import *
import customtkinter as ctk
from Register import *
from Login_graph import Login_graph




class Register_graph(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x650")
        self.title("Register Page") 
        self.configure(bg = "#c3caf7")
        self.frame = ctk.CTkFrame(self,width= 150,height= 150)
        self.frame.place( x= 200, y=70, anchor = CENTER)

        # telecharger le logo 
        self.logo = PhotoImage(file="image/logo/logoJRM1.png" )

        # Ajouter le logo à un widget Label dans le cadre
        self.logo_label = Label(self.frame, image=self.logo, bg='#c3caf7')  
        self.logo_label.pack(side=TOP)

        # titre de la page
        self.label = ctk.CTkLabel(self, text= "REGISTER", width= 50, height=50,font=('Broadway', 25), text_color="white" )
        self.label.place(x= 200, y=160, anchor = CENTER)

        # creation champ pour le prenom
        self.firstname = ctk.CTkLabel(self, text= "Firstname", width=50, height= 20, font=('Agency FB', 22, 'bold'), text_color="white")
        self.firstname.place(x=200, y=220, anchor= CENTER )
        self.entry = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        self.entry.place(x= 200, y =250, anchor = CENTER )

        # creation champ nom 
        self.surname = ctk.CTkLabel(self, text= "Surname", width=50, height=20, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.surname.place(x= 200, y= 280, anchor = CENTER)
        self.entry1 = ctk.CTkEntry(self, width=150, height=30, corner_radius= 8, fg_color= "white")
        self.entry1.place(x=200, y= 310, anchor = CENTER)

        # creation champ email
        self.email = ctk.CTkLabel(self,text= "Email", width=50, height=30,font=('Agency FB', 22, 'bold'), text_color= "white" )
        self.email.place(x=200, y=340, anchor= CENTER)
        self.entry2 = ctk.CTkEntry(self, width=200, height=30, corner_radius= 8, fg_color= "white")
        self.entry2.place(x=200, y= 370, anchor = CENTER)

        # creation champ mdp
        self.password = ctk.CTkLabel(self, text="Password", width=50, height=30, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.password.place(x=200, y=400, anchor= CENTER)
        self.entry3 = ctk.CTkEntry(self, width= 150, height=30, corner_radius= 8, fg_color="white")
        self.entry3.place(x=200, y=430, anchor = CENTER )

        # creation champ confirmer mdp
        self.password = ctk.CTkLabel(self, text="Confirm Password", width=50, height=30, font=('Agency FB', 22, 'bold'), text_color= "white")
        self.password.place(x=200, y=460, anchor= CENTER)
        self.entry4 = ctk.CTkEntry(self, width= 150, height=30, corner_radius= 8, fg_color="white")
        self.entry4.place(x=200, y=490, anchor = CENTER )

        #creation bouton valider
        self.buttonLogin = ctk.CTkButton(self, 
                                        text="VALID",
                                        width=80, 
                                        height=20,
                                        corner_radius= 10,
                                        font=("Agency FB", 21, "bold"),
                                        border_width= 2,
                                        border_color= "white",
                                        fg_color="#e74353",
                                        hover_color="#ef511c", 
                                        command= self.verifcreate_user
                                        )
        
        self.buttonLogin.place(x=200, y=550, anchor = CENTER)

    

    def verifcreate_user(self):
        register_backend = Register()   
        firstname = self.entry.get()
        surname = self.entry1.get()
        email = self.entry2.get()
        password = self.entry3.get()
        confirm_password = self.entry4.get()  # Nouvelle variable pour le mot de passe confirmé
        
        # Vérifier si les mots de passe correspondent
        if password != confirm_password:
            print("Passwords do not match!")
            # Affichez un message d'erreur à l'utilisateur ou prenez une autre action appropriée
        else:
            # Enregistrer l'utilisateur uniquement si les mots de passe correspondent
            register_backend.register(firstname, surname, email, password)
            register_backend.email_exists(email)
            # Rediriger l'utilisateur vers la page de connexion
            self.destroy()
            login = Login_graph()
            login.mainloop()


            # mise a jour de la fenetre
            self.update()

if __name__ == "__main__":
    register = Register_graph()
    register.mainloop()