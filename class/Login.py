from Server import *

class Login:
    def __init__(self):
        self.server = Server()

    def login(self, firstname, name, email, password):
        result = self.server.db.fetch(
            "SELECT id FROM user WHERE firstName=%s AND name=%s AND email=%s AND password=%s",
            (firstname, name, email, password)
        )
        
        if result:
            print("Login successful!")
            user_id = result[0][0]  
            return True, user_id  # Renvoie True et l'id_user
        else:
            print("Login failed. Please check your credentials.")
            return False, None  # Renvoie False et None