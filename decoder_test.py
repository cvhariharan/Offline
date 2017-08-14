fname = raw_input("Name: ")
f = open(fname,"r")
to_read = f.read()
#to_read = "sLqyzqR0uPNiR143Jgvpicamwx95KOAVXS2oMkh3DsIyBp1v8zC0UTPreCH2UqwjUmPD742sbk4e9Ra+iCMpUYMe9UUlkq/bMwpNtTEhtlataTLZuA9lpK6mPGppg5fEQxasfbnBK/qj0cYfW9XzcoYg1tEIXuoZEHvx/BPygUFYQvyvXVsTMr6tXmrmnad/Thz2B7sKgEqtUrcSaoFauiBo1AQa7DCCeZthpAnl+O7Ajr8xLeyIOvMHyt+KPV2VcbwqIf8CI9w="
to_read = to_read[40:]
"""key = to_read[23:55]
to_read = to_read[0:23]+to_read[55:]
#print(key)
to_read.replace(key,"")"""
import base64
from Crypto.Cipher import AES
"""
AES.key_size=128
iv="2712199708321234"

crypt_object=AES.new(key=key,mode=AES.MODE_CBC,IV=iv)

decoded=base64.b64decode(to_read) # your ecrypted and encoded text goes here
decrypted=crypt_object.decrypt(decoded)
print(decrypted)
"""
print(base64.b64decode(base64.b64decode(to_read)))
