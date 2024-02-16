from Server import *

class Login:

    def __init__(self, db):
        self.db = db

    def login(self):
        firstname = input("Enter your first name: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        result = Server.db.fetch(
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

# Quand vous utilisez la classe Login :
        
if __name__ == "__main__":
    user_manager = Login()
    login_success, user_id = user_manager.login()

    if login_success:
        print(f"User ID is: {user_id}")
    else:
        print("Login failed.")