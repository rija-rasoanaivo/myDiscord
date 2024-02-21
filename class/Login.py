from Server import *

class Login:
    def __init__(self):
        self.server = Server()
        self.user_id = None  # Initialisez user_id à None au début

    def login(self, email, password):
        self.email = email
        self.password = password
        result = self.server.db.fetch(
            "SELECT id FROM user WHERE email=%s AND password=%s",
            (email, password)
        )
        
        if result:
            print("Login successful!")
            self.user_id = result[0][0]  # Stockez l'ID de l'utilisateur dans user_id
            return True, self.user_id  # Renvoie True et l'id_user
        else:
            print("Login failed. Please check your credentials.")
            return False, None  # Renvoie False et None

    # récupérer les informations de l'utilisateur à partir de son ID
    def get_user_info(self):
        if self.user_id:
            user_info = self.server.db.fetch(
                "SELECT first_name, last_name, email FROM user WHERE id=%s",
                (self.user_id,)
            )

            print(user_info)
            return user_info
        else:
            print("No user logged in.")
            return None

    