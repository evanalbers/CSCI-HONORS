"""
This is the market class. It is a TCP server, which allows constant communication between agents and the market. The market is designed 
with the following guiding principles:
    - Agent submit Bids and Asks
    - The Market matches the lowest ask to the highest bid. If the lowest ask is lower than the highest bid, it splits the difference 
    - A transaction occurs when a match is made. The price of the transaction becomes the price of the instrument. 
    - Agents have no information regarding order depth, identity, or any information excepting the price of the instrument. 

"""

import socketserver



class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2')

class Market:

    def __init__(instrument_id, starting_price):

        bids = []
        asks = []
        price = 0


        with SimpleXMLRPCServer(('localhost', 8000),
         requestHandler=RequestHandler) as server:
         
         server.register_introspection_functions()

         def get_price():
            return price

         def place_ask(ask):

         def place_bid(bid):

         
