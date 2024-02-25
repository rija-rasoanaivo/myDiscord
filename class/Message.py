from PrivateChatRoom import *
from Login import *
from datetime import datetime

class Message:

    def __init__(self, user_id, first_name, id_room):
        self.user_id = user_id
        self.id_room = id_room
        self.first_name = first_name
        
        self.db = Server.db

    def send_message(self, message_content):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Construct the SQL query to insert the new message
        query = """
            INSERT INTO message (id_user, firstName, id_room, message_content, hour)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        # Execute the query
        self.db.executeRequete(query, (self.user_id, self.first_name, self.id_room, message_content, timestamp))
