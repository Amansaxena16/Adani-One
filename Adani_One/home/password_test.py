from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("Key.key","bw") as f:
    f.write(key)

with open("Adani_One/Key.key","rb") as f:
    key = f.read()

print(key)

# Create a Fernet instance with the key
cipher_suite = Fernet(key)

# Password to encrypt
password = b'kanpurnanimation'

# Encrypt the password
encrypted_password = cipher_suite.encrypt(password)
print("Encrypted Password:", encrypted_password)

# Decrypt the password
decrypted_password = cipher_suite.decrypt(encrypted_password)
message = decrypted_password.decode('utf-8')
print("Decrypted Password:", message)
