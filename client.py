import socket
from easygui import enterbox

mess = bytes(enterbox(msg='Enter a message', title='message'), encoding='utf-8')
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))
client_sock.send(mess)
data = client_sock.recv(1024)
client_sock.close()
print('Received', repr(data))
