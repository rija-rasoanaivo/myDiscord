from Server import Server

class User:
    
    def register(self):
        name = input("Enter the user's name: ")
        firstname = input("Enter the user's first name: ")
        email = input("Enter the user's email: ")
        password = input("Enter the user's password: ")

        table = "user"  # Nom de la table où les utilisateurs sont stockés
        fields = "name, firstName, email, password"  # Champs de la table
        values = f"'{name}', '{firstname}', '{email}', '{password}'"  # Valeurs à insérer

        # Utilisation de l'attribut de classe db de Server pour créer un utilisateur
        Server.db.create(table, fields, values)
        print(f"User {name} {firstname} registered successfully!")

    def login(self):
        firstname = input("Enter your first name: ")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Requête pour vérifier si un utilisateur correspondant existe dans la base de données
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
