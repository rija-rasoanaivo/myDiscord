from ChatRoom import *

class PrivateChatRoom:

    def __init__(self):
        # Utilisation des informations de connexion de la classe Server
        self.db = Server.db

    def get_userNames(self):
        
        try:
            self.db = Server.db
            query = "SELECT id, firstName, name FROM user"
            result = self.db.fetch(query)
            # Here, we're creating a list of dictionaries
            listMembers = [{'id': row[0], 'name': f'{row[1]} {row[2]}'} for row in result]
            print(listMembers)
            return listMembers
        except Exception as e:
            print("Error fetching user names and IDs:", e)
            return []

    

    def admin_join_private_chat_room(self, user_id, id_room):
        print(f"Adding user {user_id} as admin to room {id_room}")
        try:
            # Connect to the database if not already connected
            self.db.connexion()
            
            # Prepare the SQL query to insert the admin record
            # Be careful with direct string insertion, this is just an example.
            # You should use parameterized queries to prevent SQL injection.
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
        # Connexion à la base de données
        self.db.connexion()
        self.user_id = user_id
        self.id_room = id_room



        # Exemple de requête SQL avec INNER JOIN et les valeurs saisies par l'utilisateur
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

        # Exécution de la requête SQL
        self.db.executeRequete(query)

        # Fermeture de la connexion à la base de données
        self.db.deconnexion()

    def admin_remove_member_private_chat_room(self):
        self.db.connexion()
        admin_user_id = input("Enter the admin user id: ")
        user_id_to_remove = input("Enter the user id to remove: ")
        id_room = input("Enter the id_room: ")

        # Vérification si l'utilisateur est bien admin de la chatRoom spécifiée
        check_admin_query = f"""
            SELECT COUNT(*)
            FROM privateChatRoom
            WHERE Id_user = '{admin_user_id}' AND Id_Room = '{id_room}' AND Type_Authorisation = 'admin';
        """

        # Exécution de la requête de vérification
        self.db.cursor.execute(check_admin_query)
        is_admin = self.db.cursor.fetchone()[0]  # Lire directement le résultat

        if is_admin > 0:
            delete_query = f"""
                DELETE FROM privateChatRoom
                WHERE Id_user = '{user_id_to_remove}' AND Id_Room = '{id_room}';
            """
            self.db.executeRequete(delete_query)  # Suppression du membre
            print("Member removed successfully.")
        else:
            print("Operation not allowed. You must be an admin of the room to remove a member.")

        self.db.deconnexion()


if __name__ == "__main__":
    join_private_chat_room = PrivateChatRoom()
    join_private_chat_room.get_userNames()