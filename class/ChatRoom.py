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

if __name__ == "__main__":
    create_chat_room = ChatRoom()
    create_chat_room.create_chat_room()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)