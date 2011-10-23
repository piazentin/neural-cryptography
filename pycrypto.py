from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def pad(s):
	BS = 16
	return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

def unpad(s):
	return s[0:-ord(s[-1])]

x = [-1,-1,-1,1,1,1,1,-1,1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,1,1,-1,1,1,-1,-1,-1]
sha = SHA256.new()
sha.update(str(x))
key = sha.digest()
mode = AES.MODE_CBC
encryptor = AES.new(key, mode)

text = pad('SYNCED'.encode('utf-8'))
ciphertext = encryptor.encrypt(text)

decryptor = AES.new(key, mode)
plain = unpad(decryptor.decrypt(ciphertext))

print ciphertext
print plain
