import socket
import threading

class User:
    def __init__(self, host='127.0.0.1', port=9001):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")
        except Exception as e:
            print(f"Error connecting to server: {e}")

    def choose_channel(self):
        channel = input("Choose a channel (A, B, C, etc.): ")
        self.client_socket.send(channel.encode("utf-8"))

    def send_message(self):
        while True:
            try:
                message = input("> ")
                if message.lower() == 'quit':
                    self.close_connection()
                    break
                self.client_socket.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error sending message: {e}")
                break

    def receive_messages(self):
        while True:
            try:
                message_from_server = self.client_socket.recv(1024).decode("utf-8")
                if not message_from_server:
                    print("Disconnected from server.")
                    break
                print(message_from_server)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def close_connection(self):
        try:
            self.client_socket.close()
            print("Connection closed.")
        except Exception as e:
            print(f"Error closing connection: {e}")

    def start(self):
        try:
            self.connect()
            self.choose_channel()
            thread_receive = threading.Thread(target=self.receive_messages)
            thread_receive.start()
            self.send_message()
        except KeyboardInterrupt:
            print("Exiting...")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.close_connection()

if __name__ == "__main__":
    user = User()
    user.start()
