import numpy as np

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

# User input
text = input("Enter the text: ")
key = input("Enter the key: ")
encrypted_text = playfair_cipher(text, key)
print("Playfair Cipher Encrypted Text:", encrypted_text)

