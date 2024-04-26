from cryptography.fernet import Fernet

# Name Character Check Program
# This Program is used to check if name is valid or not!!
def restrict_character(name):
    restricted_characters = [
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", ";", ":", "'", '"', "<", ">", ",", ".", "/", "?", "~", "\n", "\r", "\t", "'", ";", "--", "<", ">", "&",]
    
    for char in restricted_characters:
        if (char in name):
            return False
        
    return True
# Code Ends Here

# Password Length Program
def check_password_length(password):
    length = len(password)
    if(length < 8 or length > 20):   
        return False
    
    else:
        return True


# Password Salting Program 

def salting(password):
    with open("Key.key","rb") as f:
        key = f.read()

    print(type(key))

    # Create a Fernet instance with the key
    cipher_suite = Fernet(key)

    # Password to encrypt
    password = password
    print("pass = ",type(password))

    # Encrypt the password
    print(password.encode())
    print(type(password.encode()))
    encrypted_password = cipher_suite.encrypt(password.encode())
    print("Encrypted Password:", encrypted_password)
    print(type(encrypted_password))

    return encrypted_password



# def decrypted(password):
#     pass
#     # Decrypt the password
#     decrypted_password = cipher_suite.decrypt(encrypted_password)
#     print("Decrypted Password:", decrypted_password.decode())
