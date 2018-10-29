from socket import *
serverName = '172.16.15.110'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('Input lowercase sentence:')
clientSocket.send(message.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024).decode()
print(message)
print(modifiedSentence)
clientSocket.close()


