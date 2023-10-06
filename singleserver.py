import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (up to 5 clients in the queue)
server_socket.listen(5)
print("TCP server is listening on {}:{}".format(*server_address))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Accepted connection from {}:{}".format(*client_address))

while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break  # If no data is received, the client has disconnected
    print("Received from client: {}".format(data.decode()))

    # Send a response back to the client
    response = input("Enter your response (or 'exit' to quit): ")
    client_socket.send(response.encode())

# Close the client and server sockets
client_socket.close()
server_socket.close()

