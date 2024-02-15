from Server import Server
from datetime import datetime

class Message:

    def __init__(self, user_id, id_room):
        self.user_id = user_id
        self.id_room = id_room
        self.db = Server.db

    def send_message(self, message_content):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Construct the SQL query to insert the new message
        query = """
            INSERT INTO message (id_user, id_room, message_content, hour)
            VALUES (%s, %s, %s, %s)
        """
        
        # Execute the query
        self.db.executeRequete(query, (self.user_id, self.id_room, message_content, timestamp))  