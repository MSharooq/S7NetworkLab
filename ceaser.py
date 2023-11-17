def caesar_cipher(text, shift):
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

# User input
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
encrypted_text = caesar_cipher(text, shift)
print("Caesar Cipher Encrypted Text:", encrypted_text)

