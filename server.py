import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(pubkey)
key_str = str(pubkey)
key_a = key_str[10:164]
print(key_a)
message = b'Hello Blablacode.ru!'
# шифруем
key = int(key_a)
crypto = rsa.encrypt(message, rsa.PublicKey(key, 65537))
print(crypto)
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message)

