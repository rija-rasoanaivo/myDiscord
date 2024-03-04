from Server import *

class Login:
    def __init__(self):
        self.server = Server()
        # Initialize user_id and first_name to None at the start
        self.user_id = None  
        self.first_name = None  

    def login(self, email, password):
        # Store the email and password provided by the user
        self.email = email
        self.password = password
        # Execute a query to fetch the user ID and first name from the 'user' table
        # where the email and password match the provided values
        result = self.server.db.fetch(
            "SELECT id, firstName FROM user WHERE email=%s AND password=%s",
            (email, password)
        )
        
        if result:
            print("Login successful!")
            # Store the user ID and first name from the query result
            self.user_id = result[0][0]  # Stockez l'ID de l'utilisateur dans user_id
            self.first_name = result[0][1]
            # Return True, user ID, and first name
            return True, self.user_id, self.first_name  # Renvoie True et l'id_user
        else:
            print("Login failed. Please check your credentials.")
            return False, None  
        
    def logout(self):
        self.user_id = None
        print("User logged out.")