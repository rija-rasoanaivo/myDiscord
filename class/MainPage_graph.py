from tkinter import *
import customtkinter as ctk
from Register_graph import *
from ChatRoom import *
from PrivateChatRoom import *
from Chatting import *
from tkinter.constants import CENTER
from Vocal import *
import threading



class MainPage_graph(Tk):
    def __init__(self, user_id=None, first_name=None):
        super().__init__()

        self.classLogin = Login()
        self.chat_room = ChatRoom()
        self.private_chat_room = PrivateChatRoom()
        self.user_id = user_id
        self.first_name = first_name

        # Initialisation de l'attribut recording
        self.recording = False
        self.voice_thread = None
        self.voice=None
        self.server=Server()
        self.server_started = False

        # Création de la fenêtre principale
        self.geometry("800x650")
        self.title("Main Page")
        self.configure(bg="black")  

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
        self.imageDeconnexion = PhotoImage(file="image/boutons/deco.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonDeconnexion = ctk.CTkButton(self, image=self.imageDeconnexion, text=None, width=20, height=20, fg_color="#c7c1f2",bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command= self.returnPageLogin)
        self.buttonDeconnexion.place(x=15, y=570)

        # creation de la frame a afficher sur la droite de mon bouton salon
        self.frame2 = ctk.CTkFrame(self, width=200, height=800, corner_radius=2, fg_color="#aeb8f9")

        # creation de la frame a afficher au dessus pour creer un salon
        self.frame3 = ctk.CTkFrame(self, width=300, height=300, corner_radius=30, fg_color="#415059")

        # creation frame4 pour afficher les messages
        self.frame4 = ctk.CTkFrame(self, width=500, height=800, corner_radius=2, fg_color="#23272d")

        # creation du logo profil
        self.imageProfil = PhotoImage(file="image/boutons/profil.png")
        # Création d'un Label avec l'image chargée comme image de fond
        self.buttonProfil = ctk.CTkButton(self, image=self.imageProfil, text=None, width=20, height=20, fg_color="#c7c1f2", bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command= self.start_server)
        self.buttonProfil.place(x=10, y=100)

        self.initialize_message_input_area()
        self.should_refresh_messages = True
        self.notification_displayed = False
        
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
            self.members.winfo_ismapped()
            self.members.place_forget()
            self.combo.winfo_ismapped()
            if hasattr(self, 'combo'):
                self.combo.place_forget()
            self.label.winfo_ismapped()
            self.label.place_forget()
    

        else: # Sinon, afficher la frame3 et ses éléments
            
            self.frame3.place(x=400, y=150)

            # Création du titre de la frame
            self.titre = ctk.CTkLabel(self, text="CREATE YOUR ROOM", width=20, height=20, font=('Broadway', 22), text_color="#c7c1f2", fg_color="#415059")
            self.titre.place(x=550, y=180, anchor=CENTER)

            # Création du champ pour le nom du salon
            self.roomName = ctk.CTkLabel(self, text="Room Name", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.roomName.place(x=550, y=210, anchor=CENTER)

            self.entry_roomName = ctk.CTkEntry(self, width=100, height=30, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, text_color="black")
            self.entry_roomName.place(x=550, y=250, anchor=CENTER)

            # Création de la checkbox pour choisir salon privé ou public
            self.type_room = ctk.CTkLabel(self, text="Type Room", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.type_room.place(x=550, y=280, anchor=CENTER)

            self.checkPublic = ctk.CTkCheckBox(self, text="Public", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPublic.place(x=480, y=310, anchor=CENTER)

            self.checkPrivate = ctk.CTkCheckBox(self, text="Private", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPrivate.place(x=630, y=310, anchor=CENTER)
            
            # creation combobox pour ajouter les membres dans le salon
            self.members = ctk.CTkLabel(self, text="Add Members", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.members.place(x=550, y=340, anchor=CENTER)
            private_chat_room = PrivateChatRoom()
            listmembers = private_chat_room.get_userNames()
            member_names = [member['name'] for member in listmembers]
            
            self.combo = ctk.CTkComboBox(self, width=150, height=25, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, values=member_names)
            self.combo.place(x=550, y=370, anchor=CENTER)

            # Création du bouton "valider"
            self.buttonValid = ctk.CTkButton(self, text="VALID", text_color="#38454c", width=80, height=20, corner_radius=10, font=("Agency FB", 21, "bold"), border_width=2, border_color="white", bg_color="#415059", fg_color="#c7c1f2", hover_color="#a78ff7", command=self.join_datacreateroom)
            self.buttonValid.place(x=550, y=420, anchor=CENTER)
    
    # fermer la frame4
    def outRoombutton(self):
        if self.frame4.winfo_ismapped():
            self.frame4.place_forget()
            self.stop_refreshing_messages()


    def show_frame4(self):
        # Afficher la frame4
        self.frame4.place(x=300, y=0)

    def frame4_message(self, id_room):
        # Clear any previous messages displayed in frame4
        for widget in self.frame4.winfo_children():
            if not isinstance(widget, ctk.CTkTextbox) and not isinstance(widget, ctk.CTkButton):
                widget.destroy()

        
        self.show_frame4()

        # Fetch messages for the selected room
        self.current_chat_instance = Chatting(self.user_id, id_room)
        messages = self.current_chat_instance.load_messages(id_room, self.user_id)

        # bouton pour quitter le salon
        self.ImageoutRoom = PhotoImage(file="image/boutons/outRoom1.png")
        self.buttonOutRoom = ctk.CTkButton(self.frame4, image=self.ImageoutRoom, text=None, width=20, height=20, fg_color="#23272d", hover_color="#23b0ed", corner_radius=10, command=lambda: self.outRoombutton())
        self.buttonOutRoom.place(x=450, y=10)
        
    
        # Display messages or a placeholder if none are found
        if messages:
            for i, message in enumerate(messages):
                message_text = f"{message[1]}"
                message_label = ctk.CTkLabel(self.frame4, text=message_text, width=170, height=30, corner_radius=10,font=("Agency FB", 20, 'bold'), fg_color="#aeb8f9", bg_color="#23272d", text_color="black")
                message_label.place(x=80, y=30 + i * 70)
                
                

            for i, message in enumerate(messages):
                message_text = f"{message[2]} {message[0]}" 
                self.messageDisplay = ctk.CTkLabel(self.frame4, text=message_text, width=100, height=20, font=("Agency FB", 14, 'bold'),text_color="white", bg_color="#23272d" )
                self.messageDisplay.place(x=80, y=60 + i * 70)

            
        else:
            default_message = ctk.CTkLabel(self.frame4, text="No messages in this room.", width=200, height=20, corner_radius=10,font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9", bg_color="#aeb8f9")
            default_message.place(x=80, y=50)

    def initialize_message_input_area(self):

        # Message entry textbox
        self.text = ctk.CTkTextbox(self.frame4, width=250, height=50, corner_radius=13, fg_color="white", bg_color="#23272d", border_color="#38454c", border_width=1, text_color="black")
        self.text.place(x=200, y=600, anchor=CENTER)
        

        # Send message button
        self.imageSend = PhotoImage(file="image/boutons/envoyer1.png")
        self.buttonSend = ctk.CTkButton(self.frame4, image=self.imageSend, text=None, width=10, height=10, fg_color="#23b0ed", border_color="black", border_width=1, hover_color="#a78ff7", corner_radius=10, command=self.send_message)
        self.buttonSend.place(x=370, y=600, anchor=CENTER)

        # Voice message button
        self.imageVoice = PhotoImage(file="image/boutons/vocal.png")
        self.buttonVoice = ctk.CTkButton(self.frame4, image=self.imageVoice, text=None, width=10, height=10, fg_color="#23b0ed", border_color="black", border_width=1, hover_color="#a78ff7", corner_radius=10, command=self.toggle_voice_message)
        self.buttonVoice.place(x=430, y=600, anchor=CENTER)

        # Emoji buttons
        self.create_emoji_buttons()
        self.update
    
    
    def create_emoji_buttons(self):
        emojis = ["😃", "😁", "😂", "🤣", "😊", "😇", "😉", "😍", "😘", "💖", "🙀", "🥺", "😭", "😤"]
        x_position = 30
        buttonwidth = 10
        buttonheight = 10
        coloremoji = "#ffba49"
        
        for emoji_code in emojis:
            button = ctk.CTkButton(self.frame4, text=emoji_code,text_color=coloremoji, font=("Segoe UI Emoji", 15),width= buttonwidth, height=buttonheight, corner_radius=5, fg_color="#23272d", hover_color="#a78ff7", command=lambda e=emoji_code: self.text.insert("end", e))
            button.place(x=x_position, y=550, anchor=CENTER)
            x_position += 30  

    def toggle_voice_message(self):

        print("Toggle voice message method called")
        if not self.recording:  # Si l'enregistrement n'est pas en cours, démarrez-le
            print("Starting voice message recording")
            self.start_voice_message()
        else:  # Sinon, arrêtez l'enregistrement
            print("Stopping voice message recording")
            self.stop_voice_message()

        self.update()

    # parti vocal 
    def start_voice_message(self):
        print("Starting voice message thread")
        self.recording = True
        # Créer une instance de Vocal
        self.voice = Vocal()
        # Démarrer le thread d'enregistrement vocal
        self.voice_thread = threading.Thread(target=self.start_voice_message_thread)
        self.voice_thread.start()


    def stop_voice_message(self):
        print("Stopping voice message recording")
        self.recording = False  # Mettre à jour l'état de l'enregistrement
        # Appeler la méthode stop de l'instance de Vocal pour arrêter l'enregistrement
        if self.voice:
            self.voice.stop()
        # Si le thread d'enregistrement vocal est en cours, attendre qu'il se termine
        if self.voice_thread is not None:
            self.voice_thread.join()

    def start_voice_message_thread(self):
        if self.recording:  # Vérifier que l'enregistrement est toujours actif
            self.voice.start()
            self.recording = False  # Mettre à jour l'état de l'enregistrement lorsque celui-ci est terminé
    def start_server(self):
        if not self.server_started:  # Vérifiez si le serveur n'est pas déjà démarré
            print("Starting server thread")
            self.server_thread = threading.Thread(target=self.server.start_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.server_started = True  # Mettez à jour l'état du serveur
        else:
            print("Stopping server thread")
            self.server.stop_server()  # Arrêtez le serveur si c'est déjà démarré
            self.server_started = False  # Mettez à jour l'état du serveur

    def start_server(self):
        if not self.server_started:  # Vérifiez si le serveur n'est pas déjà démarré
            print("Starting server thread")
            self.server_thread = threading.Thread(target=self.server.start_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.server_started = True  # Mettez à jour l'état du serveur
        else:
            print("Stopping server thread")
            self.server.stop_server()  # Arrêtez le serveur si c'est déjà démarré
            self.server_started = False  # Mettez à jour l'état du serveur

    def returnPageLogin(self):
        try:
            from Login_graph import Login_graph  # Import tardif
            
            # Libérer les ressources si nécessaire
            self.voice_thread = None
            
            # Détruire la fenêtre actuelle
            self.destroy()
            
            # Créer une nouvelle instance de la page de connexion
            go_login = Login_graph()
            go_login.mainloop()

        except Exception as e:
            print("Une erreur s'est produite lors du retour à la page de connexion:", e)
        

   
     # methode pour creer un salon
    def join_datacreateroom(self):
        roomName = self.entry_roomName.get().strip()
        isPublic = self.checkPublic.get()
        isPrivate = not isPublic  

        # Create room and get ID
        chat_room = ChatRoom()
        room_id = chat_room.create_chat_room(roomName, '0' if isPublic else '1')
        if room_id:
            private_chat_room = PrivateChatRoom()
            if isPrivate:
                # Add creator as admin
                private_chat_room.admin_join_private_chat_room(self.user_id, room_id)
                selectedMemberName = self.combo.get()
                members_list = private_chat_room.get_userNames()
                selected_member_id = next((member['id'] for member in members_list if member['name'] == selectedMemberName), None)
                if selected_member_id:
                    private_chat_room.admin_add_member_private_chat_room(selected_member_id, room_id)
                # print(f"Room '{roomName}' created with ID {room_id}.")
                label = ctk.CTkLabel(self.frame3, text="Room created successfully", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="white", fg_color="#415059")
                label.place(x=550, y=450, anchor=CENTER)
                self.toggle_right_frame()
        else:
            print("Error creating the room.")


    def select_room(self, id_room):
        print(f"Selecting room with ID: {id_room}")
        room_type = self.chat_room.get_room_type(id_room)
        room_type = str(room_type).strip() # Convertir en chaîne et supprimer les espaces
        print(f"Room type: {room_type}")

        if room_type == '1': # Si le salon est privé, vérifiez l'autorisation de l'utilisateur
            auth = self.private_chat_room.get_user_authorization(self.user_id, id_room)
            print(f"User authorization: {auth}")
            if auth in ['admin', 'member']:
                print("Authorized access to private room.")
                self.frame4_message(id_room)
                self.start_refreshing_messages()
            else:
                labelDenied = ctk.CTkLabel(self, text="Access denied.", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="white", fg_color="#415059")
                labelDenied.place(x=550, y=450, anchor=CENTER)
                self.after(1000, labelDenied.destroy)
                return
        else:
            print("Access to public room.")
            self.frame4_message(id_room)
            self.start_refreshing_messages()




        
            

    def send_message(self):
        # Récupère le contenu du ctk.CTkTextbox
        message_content = self.text.get("1.0", "end-1c").strip()
        if message_content:
            # Utilise l'instance de Chatting pour envoyer le message
            self.current_chat_instance.send_message( self.user_id, self.first_name, message_content)
            self.text.delete("1.0", "end")
            
                      
            
    def refresh_messages(self):
        # Ajoutez une vérification pour voir si le rafraîchissement doit continuer
        if self.should_refresh_messages and hasattr(self, 'current_chat_instance') and self.current_chat_instance.id_room:
            self.frame4_message(self.current_chat_instance.id_room)  # Mise à jour des messages
            self.after(500, self.refresh_messages)  # Planifiez le prochain rafraîchissement
            
            
    
            
    
    def stop_refreshing_messages(self):
        # Appelez cette méthode pour arrêter le rafraîchissement
        self.should_refresh_messages = False

    def start_refreshing_messages(self):
        # Appelez cette méthode pour démarrer ou redémarrer le rafraîchissement
        self.should_refresh_messages = True
        self.refresh_messages()

    
        
    

    
    

if __name__ == "__main__":
        app = MainPage_graph()
        app.mainloop()