from ChatRoom import *

server = Server()

class PrivateChatRoom:
    
    def create_private_chat_room(self, user_id, room_id, authorization_type):
        # Insérez les informations dans la table PrivateChatRoom
        table = "privateChatRoom"
        fields = "Id_User, ID_Room, Type_Authorisation"
        values = f"{user_id}, {room_id}, '{authorization_type}'"
        Server.db.create(table, fields, values)

if __name__ == "__main__":
    # Exemple d'utilisation
    private_chat_room_manager = PrivateChatRoom()
    user_id = 1
    room_id = 10
    authorization_type = "admin"
    private_chat_room_manager.create_private_chat_room(user_id, room_id, authorization_type)


# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"