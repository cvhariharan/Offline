fname = raw_input("Name: ")
f = open(fname,"r")
to_read = f.read()
#to_read = "sLqyzqR0uPNiR143Jgvpicamwx95KOAVXS2oMkh3DsIyBp1v8zC0UTPreCH2UqwjUmPD742sbk4e9Ra+iCMpUYMe9UUlkq/bMwpNtTEhtlataTLZuA9lpK6mPGppg5fEQxasfbnBK/qj0cYfW9XzcoYg1tEIXuoZEHvx/BPygUFYQvyvXVsTMr6tXmrmnad/Thz2B7sKgEqtUrcSaoFauiBo1AQa7DCCeZthpAnl+O7Ajr8xLeyIOvMHyt+KPV2VcbwqIf8CI9w="
import base64
from Crypto.Cipher import AES

IV = 16 * '\x00'

def decrypt(enc, key):
    decobj = AES.new(key, AES.MODE_CBC, IV)
    data = decobj.decrypt(base64.b64decode(enc))
    print(str(data.decode()))

key = to_read[23:55]
to_read = to_read[0:23]+to_read[55:]
#print(key)
to_read.replace(key,"")
decrypt(to_read, key)
