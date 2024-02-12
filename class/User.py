from MyDb import MyDb

class User:
    def __init__(self, db_instance):
        self.db = db_instance

    def login(self, firstname, name, email, password):
        result = self.db.fetch("SELECT * FROM User WHERE FirstName=%s AND Name=%s AND email=%s AND password=%s", 
                            (firstname, name, email, password))
        if result:
            print("Login successful!")
            return True
        else:
            print("Login failed. Please check your credentials.")
            return False



    def register(self, name, firstname, email, password):
        table = "user"
        fields = "name, firstName, email, password"
        
        # S'assurer que la connexion est établie avant d'accéder au cursor
        self.db.connexion()
        
        # Attention : Utiliser la fonction escape du convertisseur de mysql.connector peut ne pas être sûr.
        # Cette ligne suivante est pour démonstration et n'est PAS recommandée.
        values = f"'{self.db.cursor._connection.converter.escape(name)}', " \
                f"'{self.db.cursor._connection.converter.escape(firstname)}', " \
                f"'{self.db.cursor._connection.converter.escape(email)}', " \
                f"'{self.db.cursor._connection.converter.escape(password)}'"
        
        self.db.create(table, fields, values)
        
        # N'oubliez pas de fermer la connexion une fois terminé
        self.db.deconnexion()
        
        print(f"User {name} {firstname} registered successfully!")



#create a new instance of the MyDb class
db_instance = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")

# Create a new instance of the User class
user_system = User(db_instance)

# to register a new user
user_system.register('Doe', 'John', 'john.doe@example.com', 'securepassword123')

#to login a user
user_system.login('Doe', 'John', 'john.doe@exemple.com','securepassword123')
