from Server import Server
from datetime import datetime
from Login import Login

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
        

# This would be used after a successful login and joining a room
if __name__ == "__main__":
    user_manager = Login()
    login_success, user_id = user_manager.login()

    if login_success:
        print(f"User ID is: {user_id}")
        
        # Assume that the user has joined a room and you have the room's ID
        id_room = input("Enter the id_room you have joined: ")
        
        message_client = Message(user_id, id_room)
        
        # Example of sending a message
        message_content = input("Enter your message: ")
        message_client.send_message(message_content)

    