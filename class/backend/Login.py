from Server import Server

class Login:

    def login(self):
        firstname = input("Enter your first name: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

    
        result = Server.db.fetch(
            "SELECT * FROM user WHERE firstName=%s AND name=%s AND email=%s AND password=%s",
            (firstname, name, email, password)
        )
        
        if result:
            print("Login successful!")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False 


user_manager = Login()
user_manager.login()