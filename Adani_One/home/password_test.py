from cryptography.fernet import Fernet

with open("Key.key","rb") as f:
    key = f.read()

print(key)

# Create a Fernet instance with the key
cipher_suite = Fernet(key)

# Password to encrypt
password = "aryanresidency"

# Encrypt the password
encrypted_password = cipher_suite.encrypt(password.encode())
print("Encrypted Password:", encrypted_password)

# Decrypt the password
decrypted_password = cipher_suite.decrypt(encrypted_password)
print("Decrypted Password:", decrypted_password.decode())
