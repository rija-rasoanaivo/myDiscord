from Server import *

class ChatRoom:
    def __init__(self):
        self.server = Server()
        

    def create_chat_room(self,name, type_room):
        self.name = name
        self.type_room = type_room
        
        table = "chatRoom"
        fields = "name, type_room"
        values = f"'{name}', '{type_room}'"

        # Utilisation de l'attribut de classe db de Server
        room_id = Server.db.create(table, fields, values)

        return room_id
    
    def get_chat_room_names(self):
        try:
            self.db = Server.db
            # Écrire la requête SQL pour sélectionner les noms des salons
            requete = "SELECT name FROM chatRoom"
            # Exécuter la requête et récupérer les résultats
            result = self.db.fetch(requete)
            # Convertir les résultats en une liste de noms de salon
            names = [row[0] for row in result]
            return names
        except Exception as e:
            print("Error fetching chat room names:", e)
            return []

if __name__ == "__main__":
    create_chat_room = ChatRoom()
    create_chat_room.create_chat_room()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)