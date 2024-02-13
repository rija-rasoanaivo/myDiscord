from tkinter import *
import customtkinter as ctk
from Login import Login

class MainPage(Tk):
    def __init__(self):
        super().__init__()

        # Création de la fenêtre principale
        self.geometry("800x650")
        self.title("Main Page")
        self.configure(bg="black")  # Définition de la couleur de fond de la fenêtre principale

        # Création du cadre avec la couleur de fond spécifiée
        self.frame1 = ctk.CTkFrame(self, width=100, height=800, corner_radius=0, fg_color="#c7c1f2")  # Définition de la couleur de fond du cadre
        self.frame1.place(x=0, y=0)

        # telecharger le logo placement du logo
        self.logo = PhotoImage(file="image/logo/logoJRM2.png")
        self.logo_label = Label(self, image=self.logo, bg='#c7c1f2')
        self.logo_label.pack(side="top", anchor="nw", padx=20)

        # creation bouton salon
        self.imageRoom  = PhotoImage(file="image/boutons/room.png")
            # Création d'un Label avec l'image chargée comme image de fond
        self.buttonRoom = ctk.CTkButton(self, image=self.imageRoom,text= None, width=10, height=10,fg_color="#c7c1f2",border_color="black", border_width= 1 ,hover_color="#a78ff7", command = self.toggle_right_frame)
        self.buttonRoom.pack(side="top", anchor="nw", padx=15, pady=30)

        # creation bouton deconnexion
        self.imageDeconnexion = PhotoImage(file="image/boutons/deconnexion1.png")
            # Création d'un Label avec l'image chargée comme image de fond
        self.buttonDeconnexion = ctk.CTkButton(self, image=self.imageDeconnexion, text=None, width=10, height=10, fg_color="#c7c1f2", border_color="black", border_width=1, hover_color="#a78ff7", command=self.returnLogin)
        self.buttonDeconnexion.place(x=15, y=580)

        # creation bouton cree salon
        




        # creation de la frame a afficher sur la droite de mon bouton salon
        self.frame2 = ctk.CTkFrame(self, width=200, height=800, corner_radius=0, fg_color="#aeb8f9")

        
        
    # gestion de la frame a afficher sur la droite de mon bouton salon en cliquant sur le bouton
    def toggle_right_frame(self):
        if self.frame2.winfo_ismapped():
            self.frame2.place_forget()
        else:
            self.frame2.place(x=100, y=0)
            # Création et placement des libellés pour chaque nom de salon
            salon_names = {"Salon 1", "Salon 2", "Salon 3"}
            for i, salon_name in enumerate(salon_names):
                label = ctk.CTkLabel(self.frame2, text=salon_name, width=40, height=2, font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9", )
                label.place(x=80, y=50 + i * 50)
                
                
    def returnLogin(self):
        self.destroy()
        app = Login()
        app.mainloop()
            
                
            

        

            

           
        


if __name__ == "__main__":
        app = MainPage()
        app.mainloop()
