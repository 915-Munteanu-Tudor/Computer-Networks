import socket
import random

# The server chooses a random number.
# The clients connect and send numbers to server.
# The server returns to each client a status message:


def check_winner(SRN, CRN, too_late):
    if too_late:
        return 'L'
    elif CRN < SRN:
        return 'H'
    elif CRN == SRN:
        return 'G'
    else:
        return 'S'


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5555))

random.seed()
SRN = random.randint(1, 20)
print("Server number = " + str(SRN))
clients = []
too_late = False

while True:
    data, client_address = s.recvfrom(1024)
    data_decoded = data.decode('utf-8')
    CRN = int(data_decoded)

    print()
    print("Client [" + str(client_address) + "] sent number: " + data_decoded)

    letter = check_winner(SRN, CRN, too_late)
    if letter == 'G':
        too_late = True

    print("Verdict: " + letter)

    letter_encoded = letter.encode('utf-8')
    s.sendto(letter_encoded, client_address)
