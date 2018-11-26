import rsa

(pubkey, privkey) = rsa.newkeys(512)
a = bytes(pubkey)

message = b'Hello Blablacode.ru!'

# шифруем
crypto = rsa.encrypt(message, a)
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)