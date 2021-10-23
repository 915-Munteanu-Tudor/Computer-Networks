import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(b"heyyyy", (b"192.168.78.131", 5555))
print(s.recvfrom(10))


"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.78.131",5555))
buff,addr=s.recvfrom(10)
print(buff)
s.sendto(b"hello", addr)

"""