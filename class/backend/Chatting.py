from threading import Thread
from Message import *
from Login import *
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
        self.current_room = input("Enter the chatroom id you want to join: ")
        self.load_messages()

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
        message_content = input("Enter your message: ")
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
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord") 
    chat_client = Chatting(db)
    chat_client.start_chat_session()