import json
import socket
import random
import struct
from termcolor import colored

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ("localhost", 5000)
print(colored('Connecting on %s port %s' % server_address, 'blue'))
s.connect(server_address)

CRF = random.uniform(0, 10)

try:

    # Send data
    print(colored('Number sent: ' + str(CRF), 'cyan'))
    s.send(struct.pack('!f', CRF))

    # Receive data
    data = s.recv(1024)
    data = json.loads(data.decode())
    message = data.get("message")
    print(colored('Received: ' + str(message), 'green'))

finally:
    print(colored('Closing socket', 'red'))
    s.close()
