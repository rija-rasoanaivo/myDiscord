from Server import Server

class ChatRoom:
    
    def create_chat_room(self):
        table = input("Enter the table name: ")
        fields = input("Enter the fields (comma-separated): ")
        values = input("Enter the values (comma-separated): ")

        values = "'" + values.replace(", ", "', '") + "'"

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