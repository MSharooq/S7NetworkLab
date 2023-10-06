import socket
import threading

# Server settings
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 8080

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

# Dictionary to store connected clients (client_socket: username)
clients = {}

# Function to handle client connections
def client_handler(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {username}: {message}")
                handle_message(client_socket, username, message)
            else:
                # Remove the client if the connection is closed
                if client_socket in clients:
                    del clients[client_socket]
                break
        except:
            # Remove the client if there's an error
            if client_socket in clients:
                del clients[client_socket]
            break

# Function to handle incoming messages
def handle_message(sender_socket, sender_username, message):
    parts = message.split(':', 1)  # Split the message into "recipient:message"
    if len(parts) == 2:
        recipient_name, message_body = parts
        for client_socket, username in clients.items():
            if username == recipient_name:
                try:
                    client_socket.send(f"From {sender_username}: {message_body}".encode('utf-8'))
                except:
                    print("Error sending message.")
                break

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    username = client_socket.recv(1024).decode('utf-8')
    clients[client_socket] = username
    print(f"Connected: {username}")
    client_thread = threading.Thread(target=client_handler, args=(client_socket, username))
    client_thread.start()

