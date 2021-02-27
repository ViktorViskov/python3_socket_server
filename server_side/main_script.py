#!/usr/bin/python3
# 
# Main script for server connections
# 

# 
# Import framework libs
# 

from lib.connection.lib_connection import lib_open_connect

# 
# Function for starting server
# 

def server_start(interface = '', port = 8080):

    # 
    # Start listening
    # 

    while True:

        # open connect
        lib_open_connect(interface, port)
