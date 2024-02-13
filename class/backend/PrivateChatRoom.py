from backend.ChatRoom import *

chatRoom = ChatRoom()
server = Server()

class PrivateChatRoom:
    
    def create_private_chat_room(self, authorizing_user_id):
        chat_room = ChatRoom()
        room_id = chat_room.create_chat_room()

        if chat_room.type_room == "private":
            self.set_admin_authorization(room_id, authorizing_user_id)

    def set_admin_authorization(self, room_id, user_id):
        table = "PrivateChatRoom"
        fields = "Id_User, ID_Room, Type_Authorisation"
        values = f"{user_id}, {room_id}, 'admin'"
        Server.db.create(table, fields, values)


# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"