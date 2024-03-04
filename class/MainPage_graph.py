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

        # Initialize chat room and private chat room instances
        self.classLogin = Login()
        self.user_id = user_id
        self.first_name = first_name
        self.chat_room = ChatRoom()
        self.private_chat_room1 = PrivateChatRoom()
        

        # Initialize voice message recording
        self.recording = False
        self.voice_thread = None
        self.voice=None
        self.server=Server()
        self.server_started = False

        # Create main window
        self.geometry("800x650")
        self.title("Main Page")
        self.iconbitmap("image/logo/logoJRM1.ico")
        self.configure(bg="black")  

        # Create frame1 for display logo and buttons
        self.frame1 = ctk.CTkFrame(self, width=100, height=800, corner_radius=0, fg_color="#c7c1f2")  # Définition de la couleur de fond du cadre
        self.frame1.place(x=0, y=0)

        # download logo and display it
        self.logo = PhotoImage(file="image/logo/logoJRM3.png")
        self.logo_label = Label(self, image=self.logo, bg='#c7c1f2')
        self.logo_label.pack(side="top", anchor="nw", padx=10)

        # create button go room
        self.imageRoom  = PhotoImage(file="image/boutons/message.png")
        self.buttonRoom = ctk.CTkButton(self, image=self.imageRoom,text= None, width=20, height=20, fg_color="#c7c1f2",border_color="black",bg_color="#c7c1f2",  corner_radius=10 ,hover_color="#a78ff7", command = self.toggle_right_frame)
        self.buttonRoom.pack(side="top", anchor="nw", padx=15, pady=100)

        # create button deconnexion
        self.imageDeconnexion = PhotoImage(file="image/boutons/deco.png")
        self.buttonDeconnexion = ctk.CTkButton(self, image=self.imageDeconnexion, text=None, width=20, height=20, fg_color="#c7c1f2",bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command= self.returnPageLogin)
        self.buttonDeconnexion.place(x=15, y=570)

        # create button add chatroom
        self.imageAdd = PhotoImage(file="image/boutons/addchat.png")
        self.buttonAdd = ctk.CTkButton(self, image=self.imageAdd, text=None, width=20, height=20, fg_color="#c7c1f2",bg_color= "#c7c1f2", hover_color="#a78ff7", corner_radius= 10, command = self.toggle_createRoom)
        self.buttonAdd.place(x=50, y=480, anchor = CENTER)

        # create label create chatroom
        self.labelAdd = ctk.CTkLabel(self, text="CREATE CHATROOM", width=15, height=20, font=('Agency FB', 13, 'bold'), text_color="white", fg_color="#c7c1f2")
        self.labelAdd.place(x=50, y=430, anchor=CENTER)

        # create frame2 for display room
        self.frame2 = ctk.CTkFrame(self, width=200, height=800, corner_radius=2, fg_color="#aeb8f9")

        # create frame3 for create room
        self.frame3 = ctk.CTkFrame(self, width=300, height=300, corner_radius=30, fg_color="#415059")

        # create frame4 for display messages
        self.frame4 = ctk.CTkFrame(self, width=500, height=800, corner_radius=2, fg_color="#23272d")

        # create button login server
        self.imageProfil = PhotoImage(file="image/boutons/pac.png")
        self.buttonserver = ctk.CTkButton(self, image=self.imageProfil, text=None, width=20, height=20, fg_color="#c7c1f2", bg_color= "#c7c1f2", corner_radius= 10, hover_color="#a78ff7", command= self.start_server)
        self.buttonserver.place(x=15, y=100)

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

    # ------------ party frame3 (create room) ----------------
                
    # method for display create room
    def toggle_createRoom(self):
        
        # if the frame3 is displayed, hide it
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
            
        else: 
            
            self.frame3.place(x=400, y=150)

            # label title
            self.titre = ctk.CTkLabel(self, text="CREATE YOUR ROOM", width=20, height=20, font=('Broadway', 22), text_color="#c7c1f2", fg_color="#415059")
            self.titre.place(x=550, y=180, anchor=CENTER)

            # label room name
            self.roomName = ctk.CTkLabel(self, text="Room Name", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.roomName.place(x=550, y=210, anchor=CENTER)

            # entry room name
            self.entry_roomName = ctk.CTkEntry(self, width=100, height=30, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, text_color="black")
            self.entry_roomName.place(x=550, y=250, anchor=CENTER)

            # label type room
            self.type_room = ctk.CTkLabel(self, text="Type Room", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.type_room.place(x=550, y=280, anchor=CENTER)

            # checkbox public
            self.checkPublic = ctk.CTkCheckBox(self, text="Public", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPublic.place(x=480, y=310, anchor=CENTER)

            # checkbox private
            self.checkPrivate = ctk.CTkCheckBox(self, text="Private", text_color="white", width=40, height=20, bg_color="#415059", corner_radius=5, border_color="white", border_width=1)
            self.checkPrivate.place(x=630, y=310, anchor=CENTER)
            
            # create label add members
            self.members = ctk.CTkLabel(self, text="Add Members", width=20, height=20, font=('Agency FB', 18, 'bold'), text_color="#c7c1f2", fg_color="#415059")
            self.members.place(x=550, y=340, anchor=CENTER)
            private_chat_room = PrivateChatRoom()
            listmembers = private_chat_room.get_userNames()
            member_names = [member['name'] for member in listmembers]
            
            self.combo = ctk.CTkComboBox(self, width=150, height=25, corner_radius=5, fg_color="white", bg_color="#415059", border_color="#38454c", border_width=1, values=member_names)
            self.combo.place(x=550, y=370, anchor=CENTER)

            # create button valid
            self.buttonValid = ctk.CTkButton(self, text="VALID", text_color="#38454c", width=80, height=20, corner_radius=10, font=("Agency FB", 21, "bold"), border_width=2, border_color="white", bg_color="#415059", fg_color="#c7c1f2", hover_color="#a78ff7", command=self.join_datacreateroom)
            self.buttonValid.place(x=550, y=420, anchor=CENTER)
    

    # ------------ party frame4 (messages) ----------------

    # close button frame4
    def outRoombutton(self):
        if self.frame4.winfo_ismapped():
            self.frame4.place_forget()
            self.stop_refreshing_messages()

    # method for display frame4
    def show_frame4(self):
        self.frame4.place(x=300, y=0)


    # method for display message
    def frame4_message(self, id_room):
        # Clear any previous messages displayed in frame4
        for widget in self.frame4.winfo_children():
            if not isinstance(widget, ctk.CTkTextbox) and not isinstance(widget, ctk.CTkButton):
                widget.destroy()

        
        self.show_frame4()

        # Fetch messages for the selected room
        self.current_chat_instance = Chatting(self.user_id, id_room)
        messages = self.current_chat_instance.load_messages(id_room, self.user_id)

        # button to close the frame4
        self.ImageoutRoom = PhotoImage(file="image/boutons/outRoom1.png")
        self.buttonOutRoom = ctk.CTkButton(self.frame4, image=self.ImageoutRoom, text=None, width=20, height=20, fg_color="#23272d", hover_color="#23b0ed", corner_radius=10, command=lambda: self.outRoombutton())
        self.buttonOutRoom.place(x=450, y=10)
        
    
        # Display messages or a placeholder if none are found
        if messages:
            for i, message in enumerate(messages):
                message_text = f"{message[1]}"
                message_label = ctk.CTkLabel(self.frame4, text=message_text, width=170, height=30, corner_radius=10,font=("Agency FB", 20, 'bold'), fg_color="#ccd2ff", bg_color="#23272d", text_color="black")
                message_label.place(x=80, y=30 + i * 70)  

            for i, message in enumerate(messages):
                message_text = f"{message[0]}  {message[2]} " 
                self.messageDisplay = ctk.CTkLabel(self.frame4, text=message_text, width=100, height=20, font=("Agency FB", 13, 'bold'),text_color="white", bg_color="#23272d" )
                self.messageDisplay.place(x=90, y=60 + i * 70)
  
        else:
            default_message = ctk.CTkLabel(self.frame4, text="No messages in this room.", width=200, height=20, corner_radius=10,font=("Agency FB", 18, 'bold'), fg_color="#aeb8f9", bg_color="#aeb8f9")
            default_message.place(x=80, y=50)

    # method for initialize message input area
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


    # ---------------------- party vocal ----------------------

    # method for toggle voice message
    def toggle_voice_message(self):
        if not self.recording:  
            print("Starting voice message recording")
            self.start_voice_message()
        else:  
            print("Stopping voice message recording")
            self.stop_voice_message()

        self.update()

        
    # method for start voice message 
    def start_voice_message(self):
        print("Starting voice message thread")
        self.recording = True
        self.voice = Vocal()
        self.voice_thread = threading.Thread(target=self.start_voice_message_thread)
        self.voice_thread.start()

    # method for stop voice message
    def stop_voice_message(self):
        print("Stopping voice message recording")
        self.recording = False  
        
        if self.voice:
            self.voice.stop()
        
        if self.voice_thread is not None:
            self.voice_thread.join()


    # method for start voice message thread
    def start_voice_message_thread(self):
        if self.recording:  
            self.voice.start()
            self.recording = False  

    # method for start server
    def start_server(self):
        if not self.server_started:  
        
            self.server_thread = threading.Thread(target=self.server.start_server)
            self.server_thread.daemon = True
            self.server_thread.start()
            self.server_started = True  
        else:
            
            self.server.stop_server()  
            self.server_started = False  


    # ------------------- party interaction db -------------------     


    def returnPageLogin(self):
        try:
            from Login_graph import Login_graph  # Import tardif
            
            self.voice_thread = None
            
            self.destroy()
            
            go_login = Login_graph()
            go_login.mainloop()

        except Exception as e:
            print("Une erreur s'est produite lors du retour à la page de connexion:", e)
        

    # method join data to createRoom graph
    def join_datacreateroom(self):
        roomName = self.entry_roomName.get().strip()
        isPublic = self.checkPublic.get()
        isPrivate = not isPublic  

        # Create room and get ID
        chat_room = ChatRoom()
        room_id = chat_room.create_chat_room(roomName, '0' if isPublic else '1')
        if room_id:
            private_chat_room = PrivateChatRoom()
            self.label_message = ctk.CTkLabel(self, text="Room created successfully !", width=50, height=20, font=('Agency FB', 35, 'bold'), text_color="white")
            self.label_message.place(x=550, y=300, anchor=CENTER)
            self.after(1000, self.label_message.destroy)
        
            if isPrivate:
                # Add creator as admin
                private_chat_room.admin_join_private_chat_room(self.user_id, room_id)
                selectedMemberName = self.combo.get()
                members_list = private_chat_room.get_userNames()
                selected_member_id = next((member['id'] for member in members_list if member['name'] == selectedMemberName), None)
                
                if selected_member_id:
                    private_chat_room.admin_add_member_private_chat_room(selected_member_id, room_id)
                
                self.label_message = ctk.CTkLabel(self, text="Room created successfully !", width=50, height=20, font=('Agency FB', 35, 'bold'), text_color="white")
                self.label_message.place(x=550, y=300, anchor=CENTER)
                self.after(1000, self.label_message.destroy)
                self.toggle_right_frame()
            self.toggle_createRoom().destroy()
            self.update()

        
    # method for select room
    def select_room(self, id_room):
        room_type = self.chat_room.get_room_type(id_room)
        room_type = str(room_type).strip() # Convert to string and remove leading/trailing spaces
        
        # verify if the room is private or public
        if room_type == '1': 
            auth = self.private_chat_room1.get_user_authorization(self.user_id, id_room)
            print(f"User authorization: {auth}")
            if auth in ['admin', 'member']:
                print("Authorized access to private room.")
                self.frame4_message(id_room)
                self.start_refreshing_messages()
            else:
                labelDenied = ctk.CTkLabel(self, text="Access denied !", width=50, height=20, font=('Agency FB', 35, 'bold'), text_color="white", fg_color="black")
                labelDenied.place(x=550, y=300, anchor=CENTER)
                self.after(1000, labelDenied.destroy)
                return
        else:
            
            self.frame4_message(id_room)
            self.start_refreshing_messages()
        
    # method for send message
    def send_message(self):
        
        message_content = self.text.get("1.0", "end-1c").strip()
        if message_content:
            
            self.current_chat_instance.send_message( self.user_id, self.first_name, message_content)
            self.text.delete("1.0", "end")
            

    # ----------------- party for refresh message ------------------   


    # method for refresh message        
    def refresh_messages(self):
        if self.should_refresh_messages and hasattr(self, 'current_chat_instance') and self.current_chat_instance.id_room:
            self.frame4_message(self.current_chat_instance.id_room)  
            self.after(1000, self.refresh_messages)  
            
    # method for stop refresh message 
    def stop_refreshing_messages(self):
        self.should_refresh_messages = False


    # method for start refresh message
    def start_refreshing_messages(self):
        self.should_refresh_messages = True
        self.refresh_messages()


if __name__ == "__main__":
        app = MainPage_graph()
        app.mainloop()
        