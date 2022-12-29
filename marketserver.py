"""
This is the market class. It is a TCP server, which allows constant communication between agents and the market. The market is designed 
with the following guiding principles:
    - Agent submit Bids and Asks
    - The Market matches the lowest ask to the highest bid. If the lowest ask is lower than the highest bid, it splits the difference 
    - A transaction occurs when a match is made. The price of the transaction becomes the price of the instrument. 
    - Agents have no information regarding order depth, identity, or any information excepting the price of the instrument. 
    - Agents "watch" the market, periodically querying for the current price. 
    - 


NOTES: 

    - Max bid is currently $1000, so too for ask
    - Max number of instruments is 20
    - these can be set dynamically, by submitting 
"""

from marketfunction import handleAgent
import socket 
import threading as t
import socketserver
import numpy as np
from matplotlib import pyplot as plt


PORT = 1026


LOCK = t.Lock()

class MarketServer(socketserver.BaseRequestHandler):

    global MAX_AGENT_ID_LENGTH 
    global MAX_PRICE_DIGITS

    def __init__(self, instrument_id, ag_id_len, price_len):

        MAX_AGENT_ID_LENGTH = ag_id_len
        MAX_PRICE_DIGITS = price_len

        #list of open connections
        self.connections = {}

        #map bids to agent id
        self.bids = {}

        #map asks to agent id
        self.asks = {}

        #current price of asset
        self.price = 100

        #instrument id of this market
        self.id = instrument_id

        #INET Streaming Socket
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #bind socket to public host, known port
        serversocket.bind(('', PORT))

        #listening, can queue up to five before refusing connection - note not max connections, 
        #simply letting server catch up here
        serversocket.listen(5)

        while True:
            #accept connection
            (clientsocket, address) = serversocket.accept()

            #threaded server, dispatching to run a thread to handle client 
            agent = t.Thread(target=handleAgent, args=(clientsocket, self))
            print("starting new agent thread...")
            print(clientsocket)
            agent.start()

    def submitBid(self, bid):
        global LOCK
        with LOCK:

            self.bids[bid.bidder] = bid
            print("bid " + bid.toString())

        

    def submitAsk(self, ask):
        global LOCK
        with LOCK:

            self.asks[ask.seller] = ask
            print("ask " + ask.toString())


    def removeBid(self, bid):
        global LOCK
        with LOCK: 
            self.bids.pop(bid)


    def removeAsk(self, ask):
        global LOCK
        with LOCK:
            self.asks.pop(ask)


    def checkMatch(self):
        global LOCK
        with LOCK:

            max_bid_price = 0
            #iterate over bids, find the minimum
            for bid in self.bids:
                print(self.bids[bid].toString())
                if self.bids[bid].price > max_bid_price:
                    max_bid_price = self.bids[bid].price
                    max_bid = bid
            
            min_ask_price = 1001
            for ask in self.asks:
                if self.asks[ask].price < min_ask_price:
                    min_ask_price = self.asks[ask].price
                    min_ask = ask
            
            if max_bid_price > min_ask_price and max_bid in self.bids and min_ask in self.asks:
                
                self.price = (max_bid_price + min_ask_price) / 2
                print("agent " + max_bid + " has purchased 1 share from agent " + min_ask + " for $" + str(self.price))
                message = "t" + str(self.price)

                self.connections[max_bid].send(message.encode())
                self.connections[min_ask].send(message.encode())
                self.bids.pop(max_bid)
                self.asks.pop(min_ask)
                
                return True
                
            else:

                return False
        
    
    