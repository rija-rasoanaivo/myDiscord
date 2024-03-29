from ChatRoom import *

class PrivateChatRoom:

    def __init__(self):
        # Utilisation des informations de connexion de la classe Server
        self.db = Server.db

    def get_userNames(self):    
        # Attempt to fetch user IDs and names from the database
        try:
            self.db = Server.db
            query = "SELECT id, firstName, name FROM user"
            result = self.db.fetch(query)
            # Create a list of dictionaries with user IDs and their full names
            listMembers = [{'id': row[0], 'name': f'{row[1]} {row[2]}'} for row in result]
            
            return listMembers
        except Exception as e:
            print("Error fetching user names and IDs:", e)
            return []

    
    def admin_join_private_chat_room(self, user_id, id_room):
        print(f"Adding user {user_id} as admin to room {id_room}")
        try:
            # Connect to the database if not already connected
            self.db.connexion()
            query = """
                INSERT INTO privateChatRoom (Id_user, Id_Room, Type_Authorisation)
                VALUES (%s, %s, 'admin');
            """
            # Execute the SQL query with parameters
            self.db.executeRequete(query, (user_id, id_room))
            
            # Commit the transaction if needed
            self.db.commit()
            
            print("User added as admin successfully")
        except Exception as e:
            print(f"An error occurred while adding admin: {e}")
        finally:
            # Close the connection if you are not using a persistent connection
            self.db.deconnexion()

    def admin_add_member_private_chat_room(self, user_id, id_room):
        self.db.connexion()
        self.user_id = user_id
        self.id_room = id_room
        # request to add a member to a private chat room
        query = f"""
            INSERT INTO privateChatRoom (Id_user, Id_Room, Type_Authorisation)
            SELECT 
                user.id, chatRoom.id_room, 'member'
            FROM 
                user
            INNER JOIN 
                chatRoom ON (1=1)
            WHERE 
                user.id = '{user_id}'
                AND chatRoom.id_room = '{id_room}';
        """

        self.db.executeRequete(query)
        self.db.deconnexion()

    def get_user_authorization(self, user_id, id_room):
        try:
            self.db = Server.db
            query = "SELECT type_authorisation FROM privateChatRoom WHERE id_user = %s AND id_room = %s"
            result = self.db.fetch(query, (user_id, id_room))
            if result:
                # Assuming 'type_authorisation' is the first column in the result as only one column is selected
                return result[0][0]  # This should be the authorization type ('admin' or 'member')
            else:
                return None  # The user is neither admin nor member of this room
        except Exception as e:
            print("Error fetching user authorization:", e)
            return None


if __name__ == "__main__":
    join_private_chat_room = PrivateChatRoom()
    join_private_chat_room.get_userNames()
