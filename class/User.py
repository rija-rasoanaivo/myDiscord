from MyDb import MyDb

class User:
    def __init__(self, db_instance):
        self.db = db_instance

    def login(self, firstname, name, email, password):
        # Check if the user exists with the given firstname, name, email, and password
        result = self.db.fetch("SELECT * FROM User WHERE Firstname=%s AND Name=%s AND Mail=%s AND Password=%s", 
                            (firstname, name, email, password))
        if result:
            print("Login successful!")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False


    def register(self, name, firstname, email, password):
        # Insert a new user into the User table
        self.db.executeRequete("INSERT INTO User (Name, Firstname, Mail, Password) VALUES (%s, %s, %s, %s)", 
                               (name, firstname, email, password))
        print(f"User {name} {firstname} registered successfully!")


#create a new instance of the MyDb class
db_instance = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")

# Create a new instance of the User class
user_system = User(db_instance)

# to register a new user
user_system.register('Doe', 'John', 'john.doe@example.com', 'securepassword123')

#to login a user
user_system.login('john.doe@example.com', 'securepassword123')
