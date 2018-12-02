import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(privkey)
privkey_str = str(privkey)
key_str = str(pubkey)
key_a = key_str[10:164]
message = str(input('Message : ')).encode('utf-8')
message = str(message)
print(type(message))
message = str(message).encode('utf-8')
print(type(message))
# шифруем
key = int(key_a)
crypto = rsa.encrypt(message, rsa.PublicKey(key, 65537)) #n e
print(crypto)
crypto = str(crypto)
print(crypto)
print(type(crypto))
crypto = str(crypto).encode('utf-8')
print(crypto[2:-1])
i = 0
new = str(crypto)
print(type(crypto))
print(new)
# d = privkey_str[174:328]
# d = int(d)
# p = privkey_str[330:412]
# p = int(p)
# q = privkey_str[414:487]
# q = int(q)
# inf = rsa.decrypt(crypto, rsa.PrivateKey(key, 65537, d, p, q)) # n e d p q
# print(inf)
