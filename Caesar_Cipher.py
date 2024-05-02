# Python Implementation of the Caesar Cipher Algorithm

# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_length = len(alphabet)

# Function to perform encryption
def encrypt_message(plain_text, key):
    cipher_text = ''
    for char in plain_text:
        char = char.lower()
        if char != ' ':
            index = alphabet.find(char)
            if index == -1:
                cipher_text += char
            else:
                new_index = (index + key) % alphabet_length
                cipher_text += alphabet[new_index]
    return cipher_text

# Function to perform decryption
def decrypt_message(cipher_text, key):
    plain_text = ''
    for char in cipher_text:
        char = char.lower()
        if char != ' ':
            index = alphabet.find(char)
            if index == -1:
                plain_text += char
            else:
                new_index = (index - key) % alphabet_length
                plain_text += alphabet[new_index]
    return plain_text

print()
print('--- CAESAR CIPHER ---')
print()

# Ask user for action
print('Do you want to encrypt or decrypt?')
user_choice = input('encode/decode: ').lower()
print()

# Encryption or decryption based on user choice
if user_choice == "encode":
    print('ENCRYPTION MODE')
    print()
    key = int(input('Enter the key: '))
    message = input('Enter the message to encrypt: ')
    encrypted_text = encrypt_message(message, key)
    print(f'CIPHERTEXT: {encrypted_text}')
        
elif user_choice == "decode":
    print('DECRYPTION MODE')
    print()
    key = int(input('Enter the key: '))
    message = input('Enter the message to decrypt: ')
    decrypted_text = decrypt_message(message, key)
    print(f'PLAINTEXT: {decrypted_text}')
else:
    print("Invalid input. Please type 'encode' or 'decode'.")
  
