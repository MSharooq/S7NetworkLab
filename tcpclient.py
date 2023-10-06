import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  
port=12345
client_socket.connect((host, port))
message = input("Enter message ")
client_socket.send(message.encode('utf-8'))
response = client_socket.recv(1024) 
print(f"Server says: {response.decode('utf-8')}")
client_socket.close()

