from ChatRoom import ChatRoom

class PrivateChatRoom:

    def create_private_chat_room(self):

        name = input("Enter the room name: ")
        id_user = input("Enter the user id: ")
        id_room = input("Enter the room id: ")
        type_authorisation = input("Enter the type of authorisation: ")

        table = "privateChatRoom"
        fields = "name, id_user, id_room, type_authorisation"
        values = f"'{name}', '{id_user}', '{id_room}', '{type_authorisation}'"


        # Appel de la méthode create_chat_room() de l'instance de ChatRoom
        ChatRoom.db.create(table, fields, values)

# Utilisation de la classe PrivateChatRoom
private_chat_room_manager = PrivateChatRoom()
private_chat_room_manager.create_private_chat_room()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"