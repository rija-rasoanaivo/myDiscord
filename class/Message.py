from PrivateChatRoom import *
from Login import *
from datetime import datetime
from plyer import notification

class Message:

    def __init__(self, user_id,first_name, id_room):
        self.user_id = user_id
        self.id_room = id_room
        self.first_name = first_name
        
        self.db = Server.db

    def send_message(self, message_content):
        # Get the current timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        
        # Construct the SQL query to insert the new message
        query = """
            INSERT INTO message (id_user,firstName, id_room, message_content, hour)
            VALUES (%s,%s, %s, %s, %s)
        """
        
        # Execute the query
        self.db.executeRequete(query, (self.user_id,self.first_name, self.id_room, message_content, timestamp))  
        self.notify_user(message_content)

    def notify_user(self, message_content):
        notification.notify(
            title="New message",
            message= (f"You have a new message from {self.first_name}: {message_content}")[:50],
            timeout=10
        )

        if self.first_name == 'login':
            notification.notify(
                title="New message",
                message= (f"You have a new message from {self.first_name}: {message_content}")[:50],
                timeout=10,
            )
