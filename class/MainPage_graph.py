from tkinter import *
import customtkinter as ctk
from Register_graph import *


class MainPage_graph(Tk):
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
        self.logo = PhotoImage(file="image/logo/logoJRM3.png")
        self.logo_label = Label(self, image=self.logo, bg='#c7c1f2')
        self.logo_label.pack(side="top", anchor="nw", padx=15)

        # creation bouton salon
        self.imageRoom  = PhotoImage(file="image/boutons/room.png")
            # Création d'un Label avec l'image chargée comme image de fond
        self.buttonRoom = ctk.CTkButton(self, image=self.imageRoom,text= None, corner_radius=10, width=10, height=10,fg_color="#c7c1f2",border_color="black", border_width= 1 ,hover_color="#a78ff7", command = self.toggle_right_frame)
        self.buttonRoom.pack(side="top", anchor="nw", padx=15, pady=30)

        # creation bouton deconnexion
        self.imageDeconnexion = PhotoImage(file="image/boutons/deconnexion1.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonDeconnexion = ctk.CTkButton(self, image=self.imageDeconnexion, text=None, width=10, height=10, fg_color="#c7c1f2", border_color="black",corner_radius= 20, border_width=1, hover_color="#a78ff7", command="retour page login")
        self.buttonDeconnexion.place(x=15, y=580)

        # creation de la frame a afficher sur la droite de mon bouton salon
        self.frame2 = ctk.CTkFrame(self, width=200, height=800, corner_radius=2, fg_color="#aeb8f9")

        # creation de la frame a afficher au dessus pour creer un salon
        self.frame3 = ctk.CTkFrame(self, width=300, height=300, corner_radius=70, fg_color="#415059")

        # creation frame4 pour afficher les messages
        self.frame4 = ctk.CTkFrame(self, width=500, height=800, corner_radius=2, fg_color="#23272d")
        
    # gestion de la frame a afficher sur la droite de mon bouton salon en cliquant sur le bouton
    def toggle_right_frame(self):
        if self.frame2.winfo_ismapped():
            self.frame2.place_forget()
        else:
            self.frame2.place(x=100, y=0)
            # Création et placement des libellés pour chaque nom de salon
            salon_names = {"SALON 1", "SALON 2", "Salon 3"}
            for i, salon_name in enumerate(salon_names):
                label = ctk.CTkButton(self.frame2, text=salon_name, width=70, height=20, corner_radius=10, font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9",hover_color="#c7c1f2", border_color="white", border_width=1, command= self.frame4_message)
                label.place(x=80, y=50 + i * 50)

                # creation bouton ajouter salon
                self.imageAdd = PhotoImage(file="image/boutons/ajout.png")
                self.buttonAdd = ctk.CTkButton(self.frame2, image=self.imageAdd, text=None, width=10, height=10, fg_color="#aeb8f9", border_color="black", border_width=1, hover_color="#a78ff7",corner_radius= 10, command = self.toggle_createRoom)
                self.buttonAdd.place(x=100, y=580, anchor = CENTER)

                # texte pour ajouter un salon
                self.labelAdd = ctk.CTkLabel(self.frame2, text="clic for create Room", width=20, height=20, font=('Agency FB', 15, 'bold'), text_color="white", fg_color="#aeb8f9")
                self.labelAdd.place(x=100, y=530, anchor=CENTER)

    def toggle_createRoom(self):
        # Si la frame3 est déjà affichée, la faire disparaître et détruire ses éléments
        if self.frame3.winfo_ismapped():
            self.frame3.place_forget()
            self.label.winfo_ismapped()
            self.label.place_forget()
            self.roomName.winfo_ismapped()
            self.roomName.place_forget()
            self.entry_roomName.winfo_ismapped()
            self.entry_roomName.place_forget()
            self.type_room.winfo_ismapped()
            self.type_room.place_forget()
            self.checkPublic.winfo_ismapped()
            self.checkPublic.place_forget()
            self.checkPrivate.winfo_ismapped()
            self.checkPrivate.place_forget()
            self.members.winfo_ismapped()
            self.members.place_forget()
            self.combo.winfo_ismapped()
            self.combo.place_forget()
            self.buttonLogin.winfo_ismapped()
            self.buttonLogin.place_forget()
    

        else: # Sinon, afficher la frame3 et ses éléments
            
            self.frame3.place(x=400, y=150)

            # Création du titre de la frame
            self.label = ctk.CTkLabel(self, text="CREATE YOUR ROOM", width=20, height=20, font=('Broadway', 18), text_color="#c7c1f2", fg_color="#415059")
            self.label.place(x=550, y=180, anchor=CENTER)

            # Création du champ pour le nom du salon
            self.roomName = ctk.CTkLabel(self, text="Room Name", width=20, height=20, font=('Agency FB', 15, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.roomName.place(x=550, y=220, anchor=CENTER)

            self.entry_roomName = ctk.CTkEntry(self, width=100, height=20, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1)
            self.entry_roomName.place(x=550, y=250, anchor=CENTER)

            # Création de la checkbox pour choisir salon privé ou public
            self.type_room = ctk.CTkLabel(self, text="Type Room", width=20, height=20, font=('Agency FB', 15, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.type_room.place(x=550, y=280, anchor=CENTER)

            self.checkPublic = ctk.CTkCheckBox(self, text="Public", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPublic.place(x=500, y=310, anchor=CENTER)

            self.checkPrivate = ctk.CTkCheckBox(self, text="Private", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPrivate.place(x=620, y=310, anchor=CENTER)

            # creation combobox pour ajouter les membres dans le salon
            self.members = ctk.CTkLabel(self, text="Add members", width=20, height=20, font=('Agency FB', 15, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.members.place(x=550, y=340, anchor=CENTER)
            comboText = ["member1", "member2", "member3", "member4", "member5"]
            self.combo = ctk.CTkComboBox(self, width=150, height=25, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, values=comboText)
            self.combo.place(x=550, y=370, anchor=CENTER)

            # Création du bouton "valider"
            self.buttonLogin = ctk.CTkButton(self, text="VALID", text_color="#38454c", width=80, height=20, corner_radius=10, font=("Agency FB", 21, "bold"), border_width=2, border_color="white", bg_color="#415059", fg_color="#c7c1f2", hover_color="#a78ff7", command="doit ajouter le salon dans la base de données")
            self.buttonLogin.place(x=550, y=410, anchor=CENTER)


    def frame4_message(self):

        if self.frame4.winfo_ismapped():
            self.frame4.place_forget()
            self.frame4.destroy()
        else:
            self.frame4.place(x=300, y=0)
            
            # creation boxtext message
            self.text = ctk.CTkTextbox(self.frame4, width=250, height=50, corner_radius=5, fg_color="white", bg_color="#23272d", border_color="#38454c", border_width=1)
            self.text.place(x=50, y=50)
           
         
    # def returnLogin(self):
    #     self.destroy()
    #     app = Login_graphic()
    #     app.mainloop()
            
                
if __name__ == "__main__":
        app = MainPage_graph()
        app.mainloop()
