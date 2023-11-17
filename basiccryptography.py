import numpy as np

def ceasar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                result += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
        else:
            result += char
    return result

def hill_cipher(text, key):
    key_matrix = np.array(key).reshape(int(len(key) ** 0.5), int(len(key) ** 0.5))
    
    # Pad the text to make its length a multiple of the key matrix size
    padding = len(key) - (len(text) % len(key))
    text += 'x' * padding
    
    # Convert text to numbers
    text_numbers = [ord(char) - ord('a') for char in text]
    
    # Reshape the text into a matrix
    text_matrix = np.array(text_numbers).reshape(len(text) // len(key), len(key))
    
    # Encrypt
    encrypted_matrix = np.dot(text_matrix, key_matrix) % 26
    encrypted_text = ''.join([chr(num + ord('a')) for sublist in encrypted_matrix for num in sublist])
    
    return encrypted_text

def playfair_cipher(text, key):
    def generate_matrix(key):
        key = key.replace("j", "i")
        key_set = sorted(set(key), key=key.index)
        key_set = [char for char in key_set if char.isalpha()]
        
        # Pad with remaining characters of the alphabet
        remaining_chars = [chr(i + ord('a')) for i in range(26) if chr(i + ord('a')) not in key_set]
        key_set += remaining_chars[:25 - len(key_set)]
        
        key_matrix = np.array(list(key_set)).reshape(5, 5)
        return key_matrix

    def find_coordinates(matrix, char):
        for i in range(5):
            for j in range(5):
                if matrix[i, j] == char:
                    return i, j

    def playfair_encrypt(text, key_matrix):
        encrypted_text = ""
        i = 0
        while i < len(text):
            char1 = text[i]
            char2 = text[i + 1] if i + 1 < len(text) else 'x'

            row1, col1 = find_coordinates(key_matrix, char1)
            row2, col2 = find_coordinates(key_matrix, char2)

            if row1 == row2:
                encrypted_text += key_matrix[row1, (col1 + 1) % 5] + key_matrix[row2, (col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += key_matrix[(row1 + 1) % 5, col1] + key_matrix[(row2 + 1) % 5, col2]
            else:
                encrypted_text += key_matrix[row1, col2] + key_matrix[row2, col1]

            i += 2

        return encrypted_text

    key_matrix = generate_matrix(key)
    text = text.replace("j", "i").replace(" ", "")
    encrypted_text = playfair_encrypt(text, key_matrix)
    
    return encrypted_text

# Menu
while True:
    print("\nMenu:")
    print("1. Ceasar Cipher")
    print("2. Hill Cipher")
    print("3. Playfair Cipher")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        result = ceasar_cipher(text, shift)
        print("Ceasar Cipher Encrypted Text:", result)

    elif choice == '2':
        text = input("Enter the text (lowercase): ")
        key = input("Enter the key matrix (e.g., 9 2 4 7): ").split()
        key = [int(num) for num in key]
        result = hill_cipher(text, key)
        print("Hill Cipher Encrypted Text:", result)

    elif choice == '3':
        text = input("Enter the text: ")
        key = input("Enter the key: ")
        result = playfair_cipher(text, key)
        print("Playfair Cipher Encrypted Text:", result)

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

