from Server import Server

class Register:
    def __init__(self):
        self.server = Server()

    
    def register(self, firstname, name, email, password):
        self.firstname = firstname
        self.name = name
        self.email = email
        self.password = password

        # Vérifier si l'email existe déjà dans la base de données.
        if self.email_exists(email):
            print("An account with this email already exists. Please use a different email.")
        else:
            table = "user"
            fields = " firstName, name, email, password"
            values = f" '{firstname}', '{name}', '{email}', '{password}'"
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


if __name__ == "__main__":
    user_manager = Register()
    user_manager.register()