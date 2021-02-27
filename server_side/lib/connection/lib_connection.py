# 
# Functions for connections 
# 

# 
# Import libs
# 

import socket

def lib_open_connect(interface, port):

    # create socket
    sock = socket.socket()

    # reuse socket
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # interface and socket port
    sock.bind((interface, port))

    # number connections
    sock.listen(1)

    # socket for client and address
    conn , addr = sock.accept()

    # connection status
    print('Connected: %s' % str(addr))

    # start listening
    while True:

        # pack data in 1024 bytes
        data = conn.recv(1024)

        # stop if not data
        if not data:
            break

        # send response
        conn.send(data)

    # clouse connection
    conn.close()
    

    