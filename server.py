import rsa
(pubkey, privkey) = rsa.newkeys(512)
print(privkey)
privkey_str = str(privkey)
key_str = str(pubkey)
key_a = key_str[10:164]
message = input("Message: ")
message = str(message).encode('utf-8')
# шифруем
key = int(key_a)
crypto = rsa.encrypt(message, pubkey) #n e
print('Crypto :',crypto)
print(type(crypto))
crypto = str(crypto)
crypto = crypto[2:-1].encode('utf-8').decode('unicode-escape')
# print("this " + crypto)
# print(type(crypto))
# crypto = crypto.encode('unicode-escape')
# print(crypto)
# print(type(crypto))
# print("Вывод")
mybytes = crypto.encode()
print('Перевод crypto в bytes',mybytes)
print(type(mybytes))
str_mybytes = str(mybytes)
again_mybytes = eval(str_mybytes)
decoded = again_mybytes.decode('utf8')
print(decoded)
print(type(decoded))
by = str(decoded).encode()
print(by)
print(type(by))
# d = privkey_str[174:328]
# d = int(d)
# p = privkey_str[330:412]
# p = int(p)
# q = privkey_str[414:487]
# q = int(q)
# inf = rsa.decrypt(by, privkey) # n e d p q
# print(inf)
