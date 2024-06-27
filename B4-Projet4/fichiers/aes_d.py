import base64
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

BLOCK_SIZE = 16

def pad(s):
    pad_length = BLOCK_SIZE - len(s) % BLOCK_SIZE
    return s + chr(pad_length) * pad_length

def unpad(s):
    return s[:-ord(s[-1])]

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw).encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw)).decode('utf-8')

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

op = input("Do you want to 1. Encrypt data or 2. Decrypt data?\n")
if (op == '1'):
    msg = input("Enter the message to be encrypted: ")
    password = input("Enter password: ")
    encrypted = encrypt(msg, password)
    print("Encrypted:", encrypted)

elif (op == '2'):
    msg = input("Enter the message to be decrypted: ")
    password = input("Enter password used for encryption: ")
    decrypted = decrypt(msg, password)
    print("Decrypted:", decrypted)

else:
    print("Invalid option!")
