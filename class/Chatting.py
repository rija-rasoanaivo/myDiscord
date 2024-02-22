
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
        params = (id_room,)
        if self.last_message_timestamp:
            query += " AND hour > %s"
            params += (self.last_message_timestamp,)

        query += " ORDER BY hour DESC"  # Tri décroissant pour obtenir les derniers messages
        query += " LIMIT 6"  # Limite à 6 messages
        messages = self.db.fetch(query, params)

        # Inverser les messages pour les afficher dans l'ordre chronologique
        messages = messages[::-1]

        # Mise à jour de last_message_timestamp avec l'horodatage du dernier message chargé
        if messages:
            self.last_message_timestamp = messages[-1][2]  # Supposant que le troisième élément est l'horodatage

        return messages



    def send_message(self, message_content):
        # Création d'une instance de Message
        message = Message(self.user_id, self.id_room)
        # Envoi du message
        message.send_message(message_content)

    

if __name__ == "__main__":
    db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord") 
    chat_client = Chatting(db)