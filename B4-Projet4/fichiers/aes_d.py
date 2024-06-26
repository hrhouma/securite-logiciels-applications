import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
 
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
 
def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))
 
 
def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

op = input("Do you want to 1. Encrypt data or 2. Decrypt data?\n")
if (op == '1'):
	msg = input("Enter the message to be encrypted: ")
	password = input("Enter password: ")
	encrypted = encrypt(msg, password)
	print(encrypted)

elif (op == '2'):
	msg = input("Enter the message to be decrypted: ")
	password = input("Enter password used for encryption: ")
	decrypted = decrypt(msg, password)
	print(bytes.decode(decrypted))

else:
	print("Invalid option!")
