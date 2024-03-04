from Server import Server

class Register:
    def __init__(self):
        self.server = Server()

    # method to register a new user
    def register(self, firstname, name, email, password):
        self.firstname = firstname
        self.name = name
        self.email = email
        self.password = password

        
        if self.email_exists(email):
            print("An account with this email already exists. Please use a different email.")
        else:
            table = "user"
            fields = " firstName, name, email, password"
            values = f" '{firstname}', '{name}', '{email}', '{password}'"
            # insert the new user into the database
            Server.db.create(table, fields, values)
            print(f"User {name} {firstname} registered successfully!")

    # method to check if an email already exists in the database
    def email_exists(self, email):
        
        result = Server.db.fetch(
            "SELECT * FROM user WHERE email = %s",
            (email,)
        )
        return bool(result)  # returns True if the email exists, False otherwisea


if __name__ == "__main__":
    user_manager = Register()
    user_manager.register()