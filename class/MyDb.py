import mysql.connector

class MyDb:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connexion(self):
        self.db = mysql.connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password, 
            database=self.database
        ) 
        self.cursor = self.db.cursor()

    def deconnexion(self):
        self.db.close()

    def executeRequete(self, requete, params=None):
        self.connexion()
        self.cursor.execute(requete, params or ())
        self.db.commit()
        self.deconnexion()

    def fetch(self, requete, params=None):
        self.connexion()
        self.cursor.execute(requete, params or ())
        result = self.cursor.fetchall()
        self.deconnexion()
        return result 
    
    def create(self, table, fields, values):
        requete = "INSERT INTO " + table + " (" + fields + ") VALUES (" + values + ")"
        self.executeRequete(requete)

    def read(self, table, fields, condition):
        requete = "SELECT " + fields + " FROM " + table + " WHERE " + condition
        return self.fetch(requete)
    
    def update(self, table, fields, condition):
        requete = "UPDATE " + table + " SET " + fields + " WHERE " + condition
        self.executeRequete(requete)

    def delete(self, table, condition):
        requete = "DELETE FROM " + table + " WHERE " + condition
        self.executeRequete(requete)

# test code
# db = MyDb("82.165.185.52", "marijo", "Rijoma13!", "manon-rittling_mydiscord")
# db.connexion()

# table = "chatRoom"
# fields = "name, type_room"
# values = "'chatRoom2', 'private'"
# db.create(table, fields, values)

# table = "chatRoom"
# fields = "name = 'chatRoom1'"
# condition = "id_room = 1"
# db.update(table, fields, condition)

# table = "chatRoom"
# condition = "id_room = 3"
# db.delete(table, condition)



# db.deconnexion()








