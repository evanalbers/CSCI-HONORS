"""
A file to contain functions used by agent in watching a given instrument, used in 
multi-threading for some given agent; ie, if an agent wants to watch a given
instrument, they will spawn a thread running the overarching watch function, which
will call any helper functions in this file.

AUTHOR: Evan Albers
DATE: 8 November 2022

"""

import socket
import time as t

HOST = "localhost"
PORT = 1026
TESTMSG = "b003100"

def watch(agent, instrument_id):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True: 
            agent.evaluate(instrument_id, s)
            t.sleep(2)






