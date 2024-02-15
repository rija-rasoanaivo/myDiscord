from Server import Server

class User:
    
    def register(self):
        # Demander à l'utilisateur de saisir ses informations personnelles pour l'inscription.
        name = input("Enter the user's name: ")
        firstname = input("Enter the user's first name: ")
        email = input("Enter the user's email: ")
        password = input("Enter the user's password: ")

        # Vérifier si l'email existe déjà dans la base de données.
        if self.email_exists(email):
            print("An account with this email already exists. Please use a different email.")
        else:
            table = "user"
            fields = "name, firstName, email, password"
            values = f"'{name}', '{firstname}', '{email}', '{password}'"
            # Utilisation de la méthode 'create' pour insérer le nouvel utilisateur dans la base de données.
            Server.db.create(table, fields, values)
            print(f"User {name} {firstname} registered successfully!")

    def email_exists(self, email):
        # Exécution d'une requête pour chercher si l'email existe déjà.
        result = Server.db.fetch(
            "SELECT * FROM user WHERE email = %s",
            (email,)
        )
        return bool(result)  # Retourne True si l'email existe, False sinon.

    def login(self):
        name = input("Enter your name: ")
        firstname = input("Enter your first name: ")
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


user_manager = User()
user_manager.register()
