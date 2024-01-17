import os
from cryptography.fernet import Fernet

def encrypt_file(filepath):
   key = Fernet.generate_key()
   fernet = Fernet(key)

   with open(filepath, "rb") as file:
       original_data = file.read()

   encrypted_data = fernet.encrypt(original_data)

   with open(filepath, "wb") as file:
       file.write(encrypted_data)

   os.remove(filepath + ".enc")  # Remove any existing encrypted file
   os.rename(filepath, filepath + ".enc")  # Rename the encrypted file

   print("File encrypted successfully!")
   print("Key:", key.decode())  # Display the key for decryption

def decrypt_file(filepath):
   with open(filepath, "rb") as file:
       encrypted_data = file.read()

   key = input("Enter the key: ").encode()
   fernet = Fernet(key)

   try:
       decrypted_data = fernet.decrypt(encrypted_data)

       with open(filepath[:-4], "wb") as file:  # Remove ".enc" extension
           file.write(decrypted_data)

       os.remove(filepath)  # Remove the encrypted file
       print("File decrypted successfully!")
   except InvalidToken as e:
       print("Invalid key or file format.")

def encrypt_message(message):
   key = Fernet.generate_key()
   fernet = Fernet(key)
   encrypted_message = fernet.encrypt(message.encode())
   print("Encrypted message:", encrypted_message.decode())
   print("Key:", key.decode())

def decrypt_message(message):
   key = input("Enter the key: ").encode()
   fernet = Fernet(key)
   try:
       decrypted_message = fernet.decrypt(message.encode()).decode()
       print("Decrypted message:", decrypted_message)
   except InvalidToken as e:
       print("Invalid key or message format.")

if __name__ == "__main__":
   mode = int(input("Select mode:\n1. Encrypt file\n2. Decrypt file\n3. Encrypt message\n4. Decrypt message\nEnter your choice: "))

   if mode == 1:
       filepath = input("Enter the file path: ")
       encrypt_file(filepath)
   elif mode == 2:
       filepath = input("Enter the encrypted file path: ")
       decrypt_file(filepath)
   elif mode == 3:
       message = input("Enter the message to encrypt: ")
       encrypt_message(message)
   elif mode == 4:
       message = input("Enter the encrypted message: ")
       decrypt_message(message)
   else:
       print("Invalid mode.")
