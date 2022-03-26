import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))

while True : 
	msg = s.recv(20)
	print(msg.decode("utf-8")) 
