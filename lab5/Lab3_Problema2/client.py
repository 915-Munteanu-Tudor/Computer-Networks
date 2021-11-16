import socket
import random
from time import sleep
import sys

# The server chooses a random number.
# The clients connect and send numbers to server.
# The server returns to each client a status message:

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.78.134", 7777)
s.connect((server_address))
random.seed(10)


letter = ''
while letter != 'W' and letter != 'L':
    data = s.recv(100)
    nr_of_digits = data.decode('utf-8')
    print('Nr of digits: ' + nr_of_digits)

    CRN = random.randint(0, 9)
    data_encoded = str(CRN).encode('utf-8')
    s.send(data_encoded)
    sleep(int(sys.argv[1]))
    print("Number sent to server = " + str(CRN))


