import socket

IP = "127.0.0.1"
PORT = 5000


def no_of_redundant_bits(message):
    m = len(message)
    for r in range(m):
        if 2**r >= m + r + 1:
            return r


def find_error(message, rbits):
    m = len(message)
    error = 0

    for i in range(rbits):
        val = 0
        for j in range(1, m + 1):
            if j & (2**i) == (2**i):
                val = val ^ int(message[-j])  # Fix here
        error += val * (2**i)  # Fix here

    error = str(error)

    return "0" * (rbits - len(error)) + error


def remove_error(message, error_pos):
    corrected_message = message[:error_pos] + ("0" if message[error_pos] == "1" else "1") + message[error_pos + 1:]
    return corrected_message


def main():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    client, addr = server.accept()
    message = client.recv(1024).decode()
    if message:
        print("CLIENT >>", message)
        rbits = no_of_redundant_bits(message)
        error = find_error(message, rbits)
        check = "0" * rbits
        if error == check:
            print("SERVER >> No error in data")
        else:
            error_pos = int(error, 2)
            corrected_message = remove_error(message, error_pos)
            print("SERVER >> Error found at position", error_pos)
            print("SERVER >> Received data: ", message)
            print("SERVER >> Corrected data:", corrected_message)
    server.close()


main()


