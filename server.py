import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(privkey)
privkey_str = str(privkey)
key_str = str(pubkey)
key_a = key_str[10:164]
message = b'Hello Blablacode.ru!'
# шифруем
key = int(key_a)
crypto = rsa.encrypt(message, rsa.PublicKey(key, 65537)) #n e
print(crypto)
d = privkey_str[174:328]
d = int(d)
p = privkey_str[330:412]
p = int(p)
q = privkey_str[414:487]
q = int(q)
message = rsa.decrypt(crypto, rsa.PrivateKey(key, 65537, d, p, q)) # n e d p q
print(message)


