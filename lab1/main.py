import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#se pune ip-ul(in loc de "127.0.0.1") la care trimitem msjul dupa ce ne conectam la acelasi wi-fi
s.sendto(b"Tudor Munteanu",("127.0.0.1",7777))
print(s.recvfrom(10))