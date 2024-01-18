
# help from Edwin Pretel
#  Imports the os module for interacting with the operating system
import os
#  Imports the Fernet class from the cryptography library for symmetric encryption
from cryptography.fernet import Fernet

# Generate a random encryption key
# Creates a new random encryption key using Fernet.generate_key() and returns it
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
# Saves the given key to the specified file using open() with write-binary ('wb') mode
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

# Load the encryption key from a file
#  Reads the key from the specified file using open() with read-binary ('rb') mode and returns it
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt a file
# Creates a Fernet object using the given key
def encrypt_file(key, file_path):
    fernet = Fernet(key)
    # Opens the file in read-binary mode to read the original data
    with open(file_path, 'rb') as file:
        original_data = file.read()
    # Encrypts the data using fernet.encrypt()
    encrypted_data = fernet.encrypt(original_data)
      # Opens the file in write-binary mode and overwrites it with the encrypted data
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(key, file_path):
    # Creates a Fernet object using the given key
    fernet = Fernet(key)
    # Opens the file in read-binary mode to read the encrypted data
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        # Decrypts the data using fernet.decrypt()
    decrypted_data = fernet.decrypt(encrypted_data)
    # Opens the file in write-binary mode and overwrites it with the decrypted data
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Recursively encrypt a folder and its contents
# Recursively walks through the folder and its subfolders using os.walk()
# For each file within the folder structure, calls encrypt_file() to encrypt it
def encrypt_folder(key, folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)

# Recursively decrypt a folder that was encrypted by this tool
# Recursively walks through the folder and its subfolders using os.walk()
# For each file within the folder structure, calls decrypt_file() to decrypt it
def decrypt_folder(key, folder_path):
    # Opens the file in read-binary mode to read the encrypted data
    for root, _, files in os.walk(folder_path):
        
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(key, file_path)
# Generates a new key and saves it to a file
# Specifies the folders to encrypt and decrypt
# Calls the encrypt_folder() and decrypt_folder() functions to perform the encryption and decryption tasks
# Prints messages indicating the completion of the operations
if __name__ == "__main__":
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key, key_file)

    folder_to_encrypt = 'path/to/your/folder'
    encrypt_folder(key, folder_to_encrypt)
    print(f'Folder "{folder_to_encrypt}" encrypted.')

    folder_to_decrypt = 'path/to/your/encrypted/folder'
    decrypt_folder(key, folder_to_decrypt)
    print(f'Folder "{folder_to_decrypt}" decrypted.')
