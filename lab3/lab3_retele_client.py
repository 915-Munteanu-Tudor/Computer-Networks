"""
Set probleme cu un cuvant
Se transmite o litera de la client la server, serveru trimite inapoi litera dublata
Intoarce lungimea cuvantului
Intoarce numarul vocalelor
Intoarce numarul consoanelor
1.A client sends to the server an array of numbers. Server returns the sum of the numbers.
2.A client sends to the server a string. The server returns the count of spaces in the string.
3.A client sends to the server a string. The server returns the reversed string to the client (characters from the end to begging)
4.The client send to the server two sorted array of chars. The server will merge sort the two arrays and return the result to the client.
5.The client sends to the server an integer. The server returns the list of divisors for the specified number.
6.The client sends to the server a string and a character. The server returns to the client a list of all positions in the string where specified character is found.
7.The client sends to the server a string and two numbers (s, I, l). The sever returns to the client the substring of s starting at index I, of length l.
8.The client sends to the server two arrays of integers. The server returns an arrays containing the common numbers found in both arrays.
9.The client sends to the server two arrays of numbers. The server returns to the client a list of numbers that are present in the first arrays but not in the second.
10.The client sends to the server two strings. The server sends back the character with the largest number of occurrences on the same positions in both strings together with its count.





"""

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((b"192.168.78.132",6666))
"Pt inainte de 1, la send era: panara"
s.send(b"34567")
s.send(b"cdbadadf")
print(s.recv(45))
s.close()