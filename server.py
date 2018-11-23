import rsa

(pubkey, privkey) = rsa.newkeys(512)

message = 'Dima Pidor!'.encode('utf8')
print(pubkey)
# шифруем
crypto = rsa.encrypt(message, pubkey)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)
