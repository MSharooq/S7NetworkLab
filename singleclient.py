import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address and port to connect to
server_address = ('localhost', 12345)

# Connect to the server
client_socket.connect(server_address)
print("Connected to server.")

while True:
    # Send a message to the server
    message = input("Enter your message (or 'exit' to quit): ")
    client_socket.send(message.encode())

    if message.lower() == 'exit':
        break

    # Receive and print the server's response
    response = client_socket.recv(1024)
    print("Received from server: {}".format(response.decode()))

# Close the client socket
client_socket.close()

