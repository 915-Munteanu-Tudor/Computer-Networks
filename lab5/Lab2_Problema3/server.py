import json
import socket
import select
import struct
import random
from termcolor import colored

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

# Bind the socket to the port
server_address = ("0.0.0.0", 5000)
print('Starting up on %s port %s' % server_address)
server.bind(server_address)

# Listen for incoming connections
server.listen(10)
i = 0
inputs = [server]
outputs = []

# Server chooses the random float number between 0 and 10
SRF = random.uniform(0, 10)
closest = None
dif = 10
numbers = dict()

print(colored('Number chosen by server = ' + str(SRF), 'yellow'))

clients = []
while inputs:
    # Wait for at least one of the sockets to be ready for processing
    timeout = 10

    # SELECT
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
    if not (readable or writable or exceptional):

        print(colored('Timed out. 10 seconds passed', 'red'))

        # TODO: here we do the approximation
        dif = 10
        closest = None
        for s in numbers:
            CRF = numbers.get(s)
            if abs(SRF-CRF) <= dif:
                dif = abs(SRF-CRF)
                closest = s

        # Handle outputs
        for s in clients:
            if s in numbers:
                if s is closest:
                    print(colored("Client with socket " + str(s.getpeername()) + " won!", 'green'))
                    message = "You have the best guess with an error of " + str(dif)
                    data = json.dumps({"message": message})
                    s.sendall(data.encode())
                    # clients.remove(s)
                else:
                    message = "You lost!"
                    data = json.dumps({"message": message})
                    s.sendall(data.encode())
                    # clients.remove(s)
        break

    # Handle inputs
    for s in readable:

        if s is server:
            # A "readable" server socket is ready to accept a connection
            connection, client_address = s.accept()
            print(colored('New connection from: ' + str(client_address), 'cyan'))
            connection.setblocking(0)
            inputs.append(connection)

        else:
            data = s.recv(1024)
            if data:
                # A readable client socket has data
                CRF = struct.unpack('!f', data)
                CRF = CRF[0]
                print(colored("Received: '" + str(CRF) + "', from: " + str(s.getpeername()), 'green'))

                # TODO: do something with the number
                numbers[s] = CRF

                # Add output channel for response
                if s not in outputs:
                    outputs.append(s)
            else:
                # Interpret empty result as closed connection
                print(colored('Closing' + str(client_address) + ' after reading no data', 'magenta'))
                # Stop listening for input on the connection
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()

                # TODO: delete array if you have one
                del numbers[s]

    # Handle outputs
    for s in writable:
        if s in numbers:
            CRF = numbers.get(s)
            clients.append(s)
            outputs.remove(s)
            # try:
            #     CRF = numbers.get(s)
            # except KeyError:
            #     # No messages waiting so stop checking for writability.
            #     print(colored('No number value for client with socket: ' + str(s.getpeername()), 'yellow'))
            #     outputs.remove(s)
            # else:
            #     print(colored("Sending: '" + str(CRF) + "' to: '" + str(s.getpeername()), 'green'))
            #     s.send(struct.pack('!f', CRF))
            #     # outputs.remove(s)

    # Handle "exceptional conditions"
    for s in exceptional:
        print(colored('Handling exceptional condition for ' + str(s.getpeername()), 'yellow'))
        # Stop listening for input on the connection
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()

        # Remove message queue
        del numbers[s]
