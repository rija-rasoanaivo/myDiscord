from ChatRoom import *

class AddMember:
    def __init__(self):
        self.db = Server.db
        # Initialisation de la connexion à la base de données

    def get_userNames(self):
        try:
            # Connexion à la base de données
            self.db.connexion()

            # Requête SQL pour récupérer les noms et prénoms de tous les utilisateurs
            query = """
                SELECT firstname, name
                FROM user WHERE id;
            """

            # Exécution de la requête SQL
            self.db.fetch(query)

            # Récupération des résultats de la requête
            results = self.db.cursor.fetchall()

            

            # Retourner les résultats sous forme de liste de tuples (prénom, nom)
            return results
        except Exception as e:
            print("An error occurred while fetching user names:", str(e))
            return None

if __name__ == "__main__":
    am = AddMember()
    print(am.get_userNames())