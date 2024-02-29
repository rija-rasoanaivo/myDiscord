from Server import *

class ChatRoom:
    def __init__(self):
        self.server = Server()
        
    def create_chat_room(self, name, type_room):
        # Définition de la table, des champs et des valeurs pour l'insertion
        table = "chatRoom"
        fields = "(name, type_room)"
        values = f"('{name}', '{type_room}')"
        
        # Construction de la requête d'insertion
        query = f"INSERT INTO {table} {fields} VALUES {values};"
        
        try:
            # Connexion à la base de données via l'instance de Server.db
            Server.db.connexion()
            # Exécution de la requête avec Server.db.cursor
            Server.db.cursor.execute(query)
            # Engagement de la transaction pour s'assurer que l'insertion est réalisée
            Server.db.db.commit()
            # Récupération de l'ID de la dernière ligne insérée
            room_id = Server.db.cursor.lastrowid
            return room_id
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            # Déconnexion de la base de données
            Server.db.deconnexion()

    
    def get_chat_room_ids_and_names(self):
        try:
            self.db = Server.db
            query = "SELECT id_room, name FROM chatRoom"
            result = self.db.fetch(query)
            # Convert the results into a list of tuples (id_room, name)
            rooms = [(row[0], row[1]) for row in result]
            return rooms
        except Exception as e:
            print("Error fetching chat room IDs and names:", e)
            return []


    def get_room_type(self, id_room):
        try:
            self.db = Server.db
            query = "SELECT type_room FROM chatRoom WHERE id_room = %s"
            result = self.db.fetch(query, (id_room,))
            if result:
                # Since 'type_room' is the only column selected, it will be at index 0 of the first tuple
                return result[0][0]  # Use index 0 here
            else:
                return None
        except Exception as e:
            print("Error fetching room type:", e)
            return None


if __name__ == "__main__":
    create_chat_room = ChatRoom()
    create_chat_room.create_chat_room()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)