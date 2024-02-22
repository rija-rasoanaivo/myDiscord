
from threading import Thread
from Message import *
import time

class Chatting:
    def __init__(self, user_id, id_room):
        self.user_id = user_id
        self.id_room = id_room
        self.db = Server.db
        self.last_message_timestamp = None
    
    def load_messages(self, id_room, id_user):
        self.db = Server.db

        
        query = """
        SELECT id_user, message_content, hour
        FROM message
        WHERE id_room = %s
        """
        # Condition pour ne charger que les nouveaux messages
        params = (id_room,)
        if self.last_message_timestamp:
            query += " AND hour > %s"
            params += (self.last_message_timestamp,)

        query += " ORDER BY hour ASC"
        query += " LIMIT 7"
        messages = self.db.fetch(query, params)

        return messages


    def send_message(self, message_content):
        # Création d'une instance de Message
        message = Message(self.user_id, self.id_room)
        # Envoi du message
        message.send_message(message_content)

    # def refresh_messages(self):
    #     while True:
    #         time.sleep(3)
            
    #         query = """
    #         SELECT id_user, message_content, hour
    #         FROM message
    #         WHERE id_room = %s
    #         """
    #         params = (self.current_room,)
    #         if self.last_message_timestamp:
    #             query += " AND hour > %s"
    #             params += (self.last_message_timestamp,)

    #         query += " ORDER BY hour ASC"
    #         messages = db.fetch(query, params)  # Utilisez la nouvelle connexion ici.

    #         for id_user, content, timestamp in messages:
    #             print(f"[{timestamp}] User {id_user}: {content}")
    #             self.last_message_timestamp = timestamp

    

if __name__ == "__main__":
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord") 
    chat_client = Chatting(db)
    