from ChatRoom import ChatRoom

class PrivateChatRoom:
    def __init__(self):
        self.chat_room = ChatRoom()

    def create_private_chat_room(self):
        # Demander à l'utilisateur les informations nécessaires pour créer la salle de discussion
        table = input("Enter the table name: ")
        fields = input("Enter the fields (comma-separated): ")
        values = input("Enter the values (comma-separated): ")

        # Ajoutez des guillemets simples autour des valeurs pour les valeurs de type chaîne
        values = "'" + values.replace(", ", "', '") + "'"

        # Appel de la méthode create_chat_room() de l'instance de ChatRoom
        self.chat_room.create_chat_room(table, fields, values)

# Utilisation de la classe PrivateChatRoom
private_chat_room_manager = PrivateChatRoom()
private_chat_room_manager.create_private_chat_room()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"