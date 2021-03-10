#!/usr/bin/python3
# 
# Main script for server connections
# 

# 
# Import framework libs
# 

from lib.connection.lib_server_connection import lib_server_open_connect

# 
# Function for starting server
# 

def server_start(interface = '', port = 8080):

    # 
    # Start listening
    # 

    while True:

        # open connect
        lib_server_open_connect(interface, port)
