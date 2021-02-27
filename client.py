#!/usr/bin/python3

# import libs
import socket, json

# create socket
sock = socket.socket()

# create connection
sock.connect(('localhost', 8080))

# argumets
arg_1 = {
    'nAme': 'hello',
    'username': 'viktor'
}

json_data = json.dumps(arg_1)

print('json format > %s' % json_data)

# send data
sock.send(json_data.encode('utf-8'))

# pack data in 1024 bytes
data = sock.recv(1200)

# close connection
sock.close()

json_server_data = json.loads(data)

# print data
print('from server > %s ' % json_server_data)