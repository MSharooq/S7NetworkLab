import numpy as np

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

# User input
text = input("Enter the text (lowercase): ")
key = input("Enter the key matrix (e.g., 9 2 4 7): ").split()
key = [int(num) for num in key]
encrypted_text = hill_cipher(text, key)
print("Hill Cipher Encrypted Text:", encrypted_text)

