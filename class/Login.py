from Server import *

class Login:
    def __init__(self):
        self.server = Server()
        self.user_id = None  # Initialisez user_id à None au début
        self.first_name = None  # Initialisez first_name à None au début

    def login(self, email, password):
        self.email = email
        self.password = password
        result = self.server.db.fetch(
            "SELECT id, firstName FROM user WHERE email=%s AND password=%s",
            (email, password)
        )
        
        if result:
            print("Login successful!")
            self.user_id = result[0][0]  # Stockez l'ID de l'utilisateur dans user_id
            self.first_name = result[0][1]
            return True, self.user_id, self.first_name  # Renvoie True et l'id_user
        else:
            print("Login failed. Please check your credentials.")
            return False, None  # Renvoie False et None
        
    # méthode pour déconnecter l'utilisateur
    def logout(self):
        self.user_id = None
        print("User logged out.")

    
        


 
            

    