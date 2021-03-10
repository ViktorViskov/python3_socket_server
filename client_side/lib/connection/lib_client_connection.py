#
# Functions for client connection
#

#
# import libs
#
import socket, json

# function for open connection on client side
def lib_client_open_connection(interface, port, data):

    # create socket
    sock = socket.socket()

    # create connection
    sock.connect((interface, port))

    # convert to json
    json_data = json.dumps(data)

    # send data
    sock.send(json_data.encode('utf-8'))

    # pack data in 1024 bytes
    data = sock.recv(1200)

    # close connection
    sock.close()

    # load data from server and return
    return json.loads(data)
