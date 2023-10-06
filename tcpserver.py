import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  
port = 12345      
server_socket.bind((host, port))
server_socket.listen(5)  
print(f"Server is listening on {host}:{port}")
while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    data = client_socket.recv(1024) 
    if not data:
        break 
    print(f"Received data: {data.decode('utf-8')}")
    response = "Hello, client! This is the server."
    client_socket.send(response.encode('utf-8'))
    client_socket.close()
server_socket.close()

