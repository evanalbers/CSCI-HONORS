#AUTHOR: EVAN ALBERS
#DATE: 7 September 2022
#PURPSOE: a file that holds the classes to be used in market simulation

import random
import utilityfunction as uf
from threading import Thread
import socket
import sys
from bid import Bid as b
from ask import Ask as a
from agentfunction import watch
import universe_params as p

HOST = "localhost"

class Agent:

    """
    
    NOTES:
        - must be watching an instrument in order to evaluate / purchase it 
        - Portfolio maps instrument IDs to tuples of following form: (expected return, risk  assesment, cov. assesment)
        - General form of the "assumption set" -> set of assumptions an agent akes, that we might alter
            - pairwise covariances for every asset in their portfolio
            - expected return for every asset in their portfolio
            - expected SD for every asset in portfolio
    """

    utility_func = uf.UtilityFunction()
    watching = {}


    def __init__(self):
        
        self.id = random.randrange(10 ** (p.MAX_AGENT_ID_LENGTH)-1)

        self.capital = random.randrange(10000)

        self.portfolio = {}

        self.outstanding_bids = {}

        self.outstanding_asks = {}
    
    def evaluate(self, instrument_id, socket):

        socket.send(("p" + str(instrument_id)).encode())
        price = int(socket.recv(p.MAX_PRICE_DIGITS).decode())
        expected_return = self.watching[instrument_id][0] / price

        positive_utility = self.utility_func.calc_utility(expected_return, self.watching[instrument_id][1]) > self.utility_func.calc_utility(p.RFR, 0)

        if  positive_utility and self.capital > price and instrument_id not in self.outstanding_bids:
            self.buy(instrument_id, price, socket)

        elif not positive_utility and self.portfolio[instrument_id] > 0 and instrument_id not in self.outstanding_asks:
            self.sell(instrument_id, price, socket)
 
        else:
            expected_return = self.watching[instrument_id][0] / self.outstanding_bids[instrument_id].price + 1
            positive_utility = self.utility_func.calc_utility(expected_return, self.watching[instrument_id][1]) > self.utility_func.calc_utility(p.RFR, 0)
        
        if positive_utility and self.capital > price:
            self.buy(instrument_id, self.outstanding_bids[instrument_id].price + 1, socket)

        else: 
            expected_return = self.watching[instrument_id][0] / self.outstanding_asks[instrument_id].price - 1
            positive_utility = self.utility_func.calc_utility(expected_return, self.watching[instrument_id][1]) > self.utility_func.calc_utility(p.RFR, 0)
        
        if not positive_utility and self.portfolio[instrument_id] > 0:
            self.sell(instrument_id, price - 1, socket)        
        

    def buy(self, instrument_id, price, socket):
        if instrument_id in self.outstanding_bids:
            return

        message = 'b' + str(instrument_id) + str(price)
        self.outstanding_bids[instrument_id] = b.fromString(message)
        socket.send(message.encode())

    def sell(self, instrument_id, price, socket):
        message = 's' + str(self.id) + str(price)
        self.outstanding_asks[instrument_id] = a.fromString(message)
        socket.send(message.encode())

    def confirm(self, instrument_id, type):
        if type == 'a':
            ask = self.outstanding_asks[instrument_id]
            self.portfolio[instrument_id] -= 1
            capital += ask.price
        else:
            bid = self.outstanding_bids[instrument_id]
            self.portfolio[instrument_id] += 1
            capital -= bid.price
    
    def set_expectations(self, instrument_id, expected_value, risk):

        self.watching[instrument_id] = (expected_value, risk)

    def watch(self, instrument_id):

        self.set_expectations(instrument_id, 1000, 5)
    
        thread = Thread(target=watch, args=[self, instrument_id])
        thread.run()




    




        
