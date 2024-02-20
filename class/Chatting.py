from threading import Thread
from Message import *
import time

class Chatting:
    def __init__(self, db):
        self.db = db
        self.login_class = Login(self.db)  # Initialisez Login avec une instance de la base de données
        self.user_id = None
        self.current_room = None
        self.last_message_timestamp = None

    def login(self):
        success, user_id = self.login_class.login()
        if success:
            self.user_id = user_id
            return True
        else:
            return False

    def select_chat_room(self):
        room_id = input("Enter the chatroom id you want to join: ")
        if self.can_join_room(room_id):
            self.current_room = room_id
            self.load_messages()
            return True
        else:
            print("You do not have the permission to join this room.")
            return False

    def can_join_room(self, room_id):
        # Vérifier si la salle de chat est publique ou privée
        query = "SELECT type_room FROM chatRoom WHERE id_room = %s"
        room_type = self.db.fetch(query, (room_id,))

        if room_type:
            if room_type[0][0] == 'public':
                return True  # Tous les utilisateurs peuvent rejoindre une salle publique
            else:
                # Vérifier si l'utilisateur est admin ou membre de la salle privée
                query = """
                SELECT type_authorisation FROM privateChatRoom
                WHERE id_user = %s AND id_room = %s
                """
                user_auth = self.db.fetch(query, (self.user_id, room_id))
                # Si l'utilisateur a un enregistrement dans privateChatRoom, il peut rejoindre
                return bool(user_auth)
        else:
            print("Chat room does not exist.")
            return False
        
    def load_messages(self):
        query = """
        SELECT id_user, message_content, hour
        FROM message
        WHERE id_room = %s
        """
        #condition pour ne charger que les nouveaux messages
        params = (self.current_room,)
        if self.last_message_timestamp:
            query += " AND hour > %s"
            params += (self.last_message_timestamp,)

        query += " ORDER BY hour ASC"
        messages = self.db.fetch(query, params)

        for id_user, content, timestamp in messages:
            print(f"[{timestamp}] User {id_user}: {content}")
            self.last_message_timestamp = timestamp  # Mise à jour de l'horodatage du dernier message affiché

    def send_message(self):
        # Modification ici : pas de paramètre 'message_content' nécessaire
        # car la saisie du message est gérée directement dans cette méthode.
        message_content = input("Enter your message (or type 'CHANGE' to switch rooms): ")
        if message_content == "CHANGE":
            # L'utilisateur souhaite changer de chatroom.
            if self.select_chat_room():
                print("Switched to new chat room.")
                # Optionnel : Rafraîchir immédiatement les messages après avoir changé de chatroom.
                self.load_messages()
        else:
            # Traitement normal de l'envoi d'un message.
            message = Message(self.user_id, self.current_room)
            message.send_message(message_content)

    def refresh_messages(self):
        while True:
            time.sleep(3)
            # Créez une nouvelle connexion à chaque itération.
            db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")
            query = """
            SELECT id_user, message_content, hour
            FROM message
            WHERE id_room = %s
            """
            params = (self.current_room,)
            if self.last_message_timestamp:
                query += " AND hour > %s"
                params += (self.last_message_timestamp,)

            query += " ORDER BY hour ASC"
            messages = db.fetch(query, params)  # Utilisez la nouvelle connexion ici.

            for id_user, content, timestamp in messages:
                print(f"[{timestamp}] User {id_user}: {content}")
                self.last_message_timestamp = timestamp

    def start_chat_session(self):

        if self.login():
            if self.select_chat_room():  # S'assurer que l'utilisateur a rejoint une salle
                print("You can type 'CHANGE' at any time to switch chat rooms.")
                Thread(target=self.refresh_messages, daemon=True).start() # Démarrer un thread pour rafraîchir les messages
                while True:
                    self.send_message()  # L'utilisateur est invité à entrer un message ici, ou 'CHANGE' pour changer de salle
            else:
                print("Unable to join any chat room. Session will not start.")
        else:
            print("Login failed. Unable to start the chat session.")

if __name__ == "__main__":
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord") 
    chat_client = Chatting(db)
    chat_client.start_chat_session()