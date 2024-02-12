from Server import Server

class ChatRoom:
    
    def create_chat_room(self):
        
        name = input("Enter the fields (comma-separated): ")
        type_room = input("Enter the values (comma-separated): ")

        table = "chatRoom"
        fields = "name, type_room"
        values = f"'{name}', '{type_room}'"

        # Utilisation de l'attribut de classe db de Server
        Server.db.create(table, fields, values)

# Utilisation de la classe ChatRoom sans passer d'instance
chat_room_manager = ChatRoom()
chat_room_manager.create_chat_room()
     


# def create(self, table, fields, values):
#         requete = "INSERT INTO " + table + " (" + fields + ") VALUES (" + values + ")"
#         self.executeRequete(requete)

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)