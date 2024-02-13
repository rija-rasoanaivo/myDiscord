from ChatRoom import *

class PrivateChatRoom:

    def __init__(self):
        # Utilisation des informations de connexion de la classe Server
        self.db = Server.db

    def admin_join_private_chat_room(self):
        # Connexion à la base de données
        self.db.connexion()

        # Saisie des valeurs de user.Name et chatRoom.name par l'utilisateur
        user_id = input("Enter the user id: ")
        id_room = input("Enter the id_room: ")

        # Exemple de requête SQL avec INNER JOIN et les valeurs saisies par l'utilisateur
        query = f"""
            INSERT INTO privateChatRoom (Id_user, Id_Room, Type_Authorisation)
            SELECT 
                user.id, chatRoom.id_room, 'admin'
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

    def member_join_private_chat_room(self):
        # Connexion à la base de données
        self.db.connexion()

        # Saisie des valeurs de user.Name et chatRoom.name par l'utilisateur
        user_id = input("Enter the user id: ")
        id_room = input("Enter the id_room: ")

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

if __name__ == "__main__":
    join_private_chat_room = PrivateChatRoom()
    join_private_chat_room.admin_join_private_chat_room()
