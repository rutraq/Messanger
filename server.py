import rsa
import pickle

(pubkey, privkey) = rsa.newkeys(512)
print(pubkey)

message = b'Hello Blablacode.ru!'
# шифруем
crypto = rsa.encrypt(message, pubkey)
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)