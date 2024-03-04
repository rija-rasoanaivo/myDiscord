from Message import *

class Chatting:
    def __init__(self, user_id, id_room):
        # Initialize the Chatting instance with user ID, room ID, and database connection
        self.user_id = user_id
        self.id_room = id_room
        self.db = Server.db
        self.last_message_timestamp = None # To track the timestamp of the last loaded message
    
    def load_messages(self, id_room, id_user):
        self.db = Server.db
        # SQL query to select the first name, message content, and timestamp from the 'message' table
        # for a specific room ID

        query = """
        SELECT  firstName, message_content, hour
        FROM message
        WHERE id_room = %s
        """
        params = (id_room,)
        # If we have a timestamp for the last loaded message, append a condition to only fetch messages after that timestamp
        if self.last_message_timestamp:
            query += " AND hour > %s"
            params += (self.last_message_timestamp,)

        query += " ORDER BY hour DESC"  # Order by timestamp in descending order
        query += " LIMIT 6"  
        messages = self.db.fetch(query, params)

        # Reverse the order of the messages to display the latest message at the bottom
        messages = messages[::-1]

        # Update the last message timestamp
        if messages:
            self.last_message_timestamp = messages[::-1]  

        return messages


    def send_message(self,user_id, first_name, message_content):
        # Create a new Message instance
        message = Message(user_id=user_id, first_name=first_name, id_room= self.id_room)
        # Call the send_message method of the Message instance
        message.send_message(message_content)