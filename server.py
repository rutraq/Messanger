import rsa
import pickle
(pubkey, privkey) = rsa.newkeys(256)
print(pubkey)
print(type(pubkey))
key = pickle.dumps(pubkey)
print(type(key))
print(key)
key_str = str(key)
print(key_str)
key_1 = pickle.loads(key)
print(type(key_1))
print(key_1)
message = b'Hello Blablacode.ru!'

# шифруем
crypto = rsa.encrypt(message, key_1)
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)