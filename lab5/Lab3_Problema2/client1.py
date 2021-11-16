import socket
import random
from time import sleep

# The server chooses a random number.
# The clients connect and send numbers to server.
# The server returns to each client a status message:

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("192.168.78.134", 5555)
random.seed(10)

letter = ''
while letter != 'G' and letter != 'L':
    CRN = random.randint(1, 20)
    data_encoded = str(CRN).encode('utf-8')
    s.sendto(data_encoded, server_address)
    sleep(2)
    print("Number sent to server = " + str(CRN))

    data, addr = s.recvfrom(10)
    letter = data.decode('utf-8')
    print('Letter received back is: ' + letter)
