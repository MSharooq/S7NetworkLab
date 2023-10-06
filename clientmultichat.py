import socket
import threading

# Server settings
SERVER_HOST = '127.0.0.1'  # Change this to the server's IP address
SERVER_PORT = 8080

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Connection to the server has been closed.")
            break

# Function to send messages to the server
def send_messages(client_socket, username):
    while True:
        recipient = input("Enter the recipient's username: ")
        message = input("Enter your message: ")
        if recipient and message:
            full_message = f"{recipient}:{message}"
            client_socket.send(full_message.encode('utf-8'))

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Input username and send it to the server
username = input("Enter your username: ")
client_socket.send(username.encode('utf-8'))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
send_thread = threading.Thread(target=send_messages, args=(client_socket, username))
receive_thread.start()
send_thread.start()

