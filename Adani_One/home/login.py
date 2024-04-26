from cryptography.fernet import Fernet

def decrypted(hash_password):

    with open("Key.key","rb") as f:
        key = f.read()
    
    cipher_suite = Fernet(key)

    decrypted_password = cipher_suite.decrypt(hash_password)
    return decrypted_password
