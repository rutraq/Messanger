# import rsa
# import ast
# (pubkey, privkey) = rsa.newkeys(512)
# message = str('Соси писос').encode('UTF-8')
#
# # шифруем
# crypto = rsa.encrypt(message, pubkey)
# print('Crypto :', crypto)
# message = rsa.decrypt(ast.literal_eval(str(crypto)), privkey)
# print('Message :', message)
import rsa

pub_key, pr_key = rsa.newkeys(512)
message = 'привет'.encode('utf8')
# message = b'допустим этот?'
crypto = rsa.encrypt(message, pub_key)
print(crypto)
message = rsa.decrypt(crypto, pr_key)
print(message.decode('UTF-8'))