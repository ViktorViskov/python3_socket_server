#!/usr/bin/python3

# 
# Import libs 
# 

from lib.connection.lib_client_connection import lib_client_open_connection

addr = "localhost"
port = 8080

data = "Some data"

data_to_print = lib_client_open_connection(addr, port, data)

print(data_to_print)