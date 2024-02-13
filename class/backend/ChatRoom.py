from Server import Server

class ChatRoom:
    
    def create_chat_room(self):
        
        name = input("Enter the room name: ")
        type_room = input("Enter the room type (public/private): ")

        table = "chatRoom"
        fields = "name, type_room"
        values = f"'{name}', '{type_room}'"

        # Utilisation de l'attribut de classe db de Server
        room_id = Server.db.create(table, fields, values)

        return room_id

create_chat_room = ChatRoom()
create_chat_room.create_chat_room()


# def create(self, table, fields, values):
#         requete = "INSERT INTO " + table + " (" + fields + ") VALUES (" + values + ")"
#         self.executeRequete(requete)

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)