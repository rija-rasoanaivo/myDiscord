from tkinter import *
import customtkinter as ctk
from Register_graph import *
from ChatRoom import *
from PrivateChatRoom import *
from Chatting import *
from Vocal import Vocal
import threading



class MainPage_graph(Tk):
    def __init__(self, user_id=None, first_name=None):
        super().__init__()

        self.classLogin = Login()
        self.user_id = user_id
        self.first_name = first_name
        self.server = Server()


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
        self.logo_label.pack(side="top", anchor="nw", padx=10)

        # creation bouton salon
        self.imageRoom  = PhotoImage(file="image/boutons/sms.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonRoom = ctk.CTkButton(self, image=self.imageRoom,text= None, width=20, height=20, fg_color="#c7c1f2",border_color="black",bg_color="#c7c1f2",  corner_radius=10 ,hover_color="#a78ff7", command = self.toggle_right_frame)
        self.buttonRoom.pack(side="top", anchor="nw", padx=12, pady=70)

        # creation bouton deconnexion
        self.imageDeconnexion = PhotoImage(file="image/boutons/deconnexion1.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonDeconnexion = ctk.CTkButton(self, image=self.imageDeconnexion, text=None, width=20, height=20, fg_color="#c7c1f2",bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command= self.returnPageLogin)
        self.buttonDeconnexion.place(x=15, y=580)

        # creation de la frame a afficher sur la droite de mon bouton salon
        self.frame2 = ctk.CTkFrame(self, width=200, height=800, corner_radius=2, fg_color="#aeb8f9")

        # creation de la frame a afficher au dessus pour creer un salon
        self.frame3 = ctk.CTkFrame(self, width=300, height=300, corner_radius=30, fg_color="#415059")

        # creation frame4 pour afficher les messages
        self.frame4 = ctk.CTkFrame(self, width=500, height=800, corner_radius=2, fg_color="#23272d")

        # creation du logo profil
        self.imageProfil = PhotoImage(file="image/boutons/profil.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonProfil = ctk.CTkButton(self, image=self.imageProfil, text=None, width=20, height=20, fg_color="#c7c1f2", bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command=lambda: print(self.user_id))
        self.buttonProfil.place(x=10, y=100)
        self.initialize_message_input_area()
        
    # gestion de la frame a afficher sur la droite de mon bouton salon en cliquant sur le bouton
    def toggle_right_frame(self):
        if self.frame2.winfo_ismapped():
            self.frame2.place_forget()
        else:
            self.frame2.place(x=100, y=0)
            room_info = ChatRoom().get_chat_room_ids_and_names()
            for i, (room_id, room_name) in enumerate(room_info):
                button = ctk.CTkButton(self.frame2, text=room_name, width=70, height=20, corner_radius=10, font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9",bg_color="#aeb8f9", hover_color= "#a78ff7", command=lambda id=room_id: self.select_room(id))
                button.place(x=80, y=50 + i * 50)

                # creation bouton ajouter salon
                self.imageAdd = PhotoImage(file="image/boutons/ajout.png")
                self.buttonAdd = ctk.CTkButton(self.frame2, image=self.imageAdd, text=None, width=20, height=20, fg_color="#aeb8f9",bg_color= "#aeb8f9", hover_color="#a78ff7", corner_radius= 10, command = self.toggle_createRoom)
                self.buttonAdd.place(x=100, y=610, anchor = CENTER)

                # texte pour ajouter un salon
                self.labelAdd = ctk.CTkLabel(self.frame2, text="clic for create Room", width=20, height=20, font=('Agency FB', 15, 'bold'), text_color="white", fg_color="#aeb8f9")
                self.labelAdd.place(x=100, y=560, anchor=CENTER)

    def toggle_createRoom(self):
        # Si la frame3 est déjà affichée, la faire disparaître et détruire ses éléments
        if self.frame3.winfo_ismapped():
            self.frame3.place_forget()
            self.titre.winfo_ismapped()
            self.titre.place_forget()
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
            self.buttonValid.winfo_ismapped()
            self.buttonValid.place_forget()
            self.label.winfo_ismapped()
            self.label.place_forget()
    

        else: # Sinon, afficher la frame3 et ses éléments
            
            self.frame3.place(x=400, y=150)

            # Création du titre de la frame
            self.titre = ctk.CTkLabel(self, text="CREATE YOUR ROOM", width=20, height=20, font=('Broadway', 22), text_color="#c7c1f2", fg_color="#415059")
            self.titre.place(x=550, y=180, anchor=CENTER)

            # Création du champ pour le nom du salon
            self.roomName = ctk.CTkLabel(self, text="Room Name", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.roomName.place(x=550, y=220, anchor=CENTER)

            self.entry_roomName = ctk.CTkEntry(self, width=100, height=30, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, text_color="black")
            self.entry_roomName.place(x=550, y=260, anchor=CENTER)

            # Création de la checkbox pour choisir salon privé ou public
            self.type_room = ctk.CTkLabel(self, text="Type Room", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.type_room.place(x=550, y=300, anchor=CENTER)

            self.checkPublic = ctk.CTkCheckBox(self, text="Public", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPublic.place(x=480, y=340, anchor=CENTER)

            self.checkPrivate = ctk.CTkCheckBox(self, text="Private", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPrivate.place(x=630, y=340, anchor=CENTER)


            # Création du bouton "valider"
            self.buttonValid = ctk.CTkButton(self, text="VALID", text_color="#38454c", width=80, height=20, corner_radius=10, font=("Agency FB", 21, "bold"), border_width=2, border_color="white", bg_color="#415059", fg_color="#c7c1f2", hover_color="#a78ff7", command=self.join_datacCreateroom)
            self.buttonValid.place(x=550, y=410, anchor=CENTER)

    def voice_message(self):
        # Exécutez la fonction start dans un thread séparé
        threading.Thread(target=self.start_voice_message_thread).start()

    def start_voice_message_thread(self):
        vocal = Vocal()
        vocal.start()

    def frame4_message(self, id_room):
        for widget in self.frame4.winfo_children():
            if not isinstance(widget, ctk.CTkTextbox) and not isinstance(widget, ctk.CTkButton):
                widget.destroy()

        self.frame4.place(x=300, y=0)

        # Récupération des messages pour la salle sélectionnée
        self.current_chat_instance = Chatting(self.user_id, id_room)
        messages = self.current_chat_instance.load_messages(id_room, self.user_id)

        if messages:
            for i, message in enumerate(messages):
                message_text = f"{message[1]}"  
                # Création et placement des labels pour chaque message
                message_label = ctk.CTkLabel(self.frame4, text=message_text, width=170, height=30, corner_radius=10, font=("Agency FB", 20, 'bold'), fg_color="#aeb8f9", bg_color="#23272d", text_color="black")
                message_label.place(x=80, y=30 + i * 70)

                message_details = f"{message[2]} {message[0]}"
                details_label = ctk.CTkLabel(self.frame4, text=message_details, width=100, height=20, font=("Agency FB", 14, 'bold'), text_color="white", bg_color="#23272d")
                details_label.place(x=80, y=60 + i * 70)
        else:
            # Affichage d'un message par défaut si aucun message n'est trouvé dans la salle
            default_message = ctk.CTkLabel(self.frame4, text="No messages in this room yet.", width=200, height=20, corner_radius=10, font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9", bg_color="#23272d", text_color="white")
            default_message.place(x=150, y=50) 


    def initialize_message_input_area(self):
        # Zone de texte pour les messages
        self.text = ctk.CTkTextbox(self.frame4, width=250, height=50, corner_radius=13, fg_color="white", bg_color="#23272d", border_color="#38454c", border_width=1, text_color="black")
        self.text.place(x=200, y=600, anchor=CENTER)

        # Bouton d'envoi
        self.imageSend = PhotoImage(file="image/boutons/envoyer1.png")  # Assurez-vous que le chemin d'accès est correct
        self.buttonSend = ctk.CTkButton(self.frame4, image=self.imageSend, text=None, width=10, height=10, fg_color="#23b0ed", border_color="black", border_width=1, hover_color="#a78ff7", corner_radius=10, command=self.send_message)
        self.buttonSend.place(x=370, y=600, anchor=CENTER)

        # Bouton de message vocal
        self.imageVoice = PhotoImage(file="image/boutons/vocal.png")  # Assurez-vous que le chemin d'accès est correct
        self.buttonVoice = ctk.CTkButton(self.frame4, image=self.imageVoice, text=None, width=10, height=10, fg_color="#23b0ed", border_color="black", border_width=1, hover_color="#a78ff7", corner_radius=10, command=self.voice_message)
        self.buttonVoice.place(x=430, y=600, anchor=CENTER)

        # Boutons Emoji
        self.create_emoji_buttons()

    def create_emoji_buttons(self):
        emoji_files = ["heartred1.png", "loveheart.png", "mdr.png", "pouce.png", "eyesopen.png"]  # Assurez-vous que les chemins d'accès sont corrects
        x_position = 100
        for emoji_file in emoji_files:
            emoji_image = PhotoImage(file=f"image/emoji/{emoji_file}")
            buttonEmoticones = ctk.CTkButton(self.frame4, image=emoji_image, text=None, width=5, height=5, fg_color="#23272d", hover_color="#23b0ed")
            buttonEmoticones.place(x=x_position, y=530)
            x_position += 30
            setattr(self, emoji_file.split('.')[0], emoji_image)

              
    # methode pour retourner a la page de connexion
    def returnPageLogin(self): 
         
        self.destroy()
        go_login = Login_graph()
        go_login.mainloop()


    def join_datacCreateroom(self):
        # recupere les valeurs saisies par l'utilisateur
        roomName = self.entry_roomName.get()
        typeRoom = self.checkPublic.get()
        typeRoom = self.checkPrivate.get()

        # insertion des valeurs dans la base de données par la classe ChatRoom
        create_room = ChatRoom()
        create_room.create_chat_room(roomName, typeRoom)

        # affichage d'un message de confirmation
        self.label = ctk.CTkLabel(self, text="Room created", width=20, height=20, font=('Agency FB', 30, 'bold'), text_color="white", fg_color="#415059")
        self.label.place(x=550, y=300, anchor=CENTER)

        # ajoute l'administrateur dans le salon privé
        admin_join = PrivateChatRoom()
        admin_join.admin_join_private_chat_room()

        
        # Actualisation de la liste des salons
        self.toggle_right_frame()

    def start_server_when_room_selected(self, id_room):
        # Création du serveur et activation du socket
        self.server.create_server_socket()

    def select_room(self, id_room):
        self.id_room = id_room  # Stockez l'ID du salon sélectionné
        self.frame4_message(id_room)
        if not hasattr(self, 'refresh_initialized') or not self.refresh_initialized:
            self.refresh_messages()
            self.refresh_initialized = True

    def send_message(self):
        # Récupère le contenu du ctk.CTkTextbox
        message_content = self.text.get("1.0", "end-1c").strip()
        if message_content:
            # Utilise l'instance de Chatting pour envoyer le message
            self.current_chat_instance.send_message(self.user_id, self.first_name, message_content)
            self.text.delete("1.0", "end")
            # Rafraîchir les messages pour inclure le nouveau message

    def refresh_messages(self):
        if hasattr(self, 'current_chat_instance') and self.current_chat_instance.id_room:
            self.frame4_message(self.current_chat_instance.id_room)  # Mise à jour des messages
            self.after(10000, self.refresh_messages)

                        
                
                    
            

              
                
if __name__ == "__main__":
        app = MainPage_graph()
        app.mainloop()