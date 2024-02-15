from threading import Thread
from Message import Message
from Login import Login
from MyDb import MyDb
import time
# Assurez-vous d'importer vos classes ici. Exemple:
# from MyDb import MyDb
# from Login import Login
# from Message import Message
# from ChatRoom import ChatRoom # Si vous avez une classe pour gérer les chatrooms

class ChatClient:
    def __init__(self, db):
        # Supposons que db est une instance de votre classe MyDb ou une classe similaire pour la gestion de la base de données
        self.db = db
        self.login_class = Login(self.db)  # Initialisez Login avec une instance de la base de données
        self.user_id = None
        self.current_room = None
        self.last_message_timestamp = None

    def login(self):
        # Utilisez votre classe de login existante pour authentifier l'utilisateur
        success, user_id = self.login_class.login()
        if success:
            self.user_id = user_id
            print("Login successful!")
            return True
        else:
            print("Login failed.")
            return False

    def select_chat_room(self):
        self.current_room = input("Enter the chatroom id you want to join: ")
        self.load_messages()

    def load_messages(self):
        query = """
        SELECT id_user, message_content, hour
        FROM message
        WHERE id_room = %s
        """
        # Si on a déjà chargé des messages, on ajoute une condition pour ne charger que les nouveaux messages
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
        message_content = input("Enter your message: ")
        # Notez que nous passons seulement deux arguments ici
        message = Message(self.user_id, self.current_room)
        message.send_message(message_content)

    def refresh_messages(self):
        while True:
            time.sleep(10)
            self.load_messages()

    def start_chat_session(self):
        if self.login():
            self.select_chat_room()
            Thread(target=self.refresh_messages, daemon=True).start()
            while True:
                self.send_message()

if __name__ == "__main__":
    # Assurez-vous de créer une instance de MyDb ou de votre classe de gestion de base de données ici
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")  # Exemple, remplacez par vos vraies informations de connexion
    chat_client = ChatClient(db)
    chat_client.start_chat_session()
