#AUTHOR: EVAN ALBERS
#DATE: 7 September 2022
#PURPSOE: a file that holds the classes to be used in market simulation

import random
import riskfunction as rf
import xmlrpc.client

class Agent:

    """
    
    NOTES:
        - must be watching an instrument in order to evaluate / purchase it 
    """

    risk_func = rf.RiskFunction()
    watching = {}


    def __init__(self):
        
        self.id = random.randrange(100)

        self.capital = random.randrange(100)

        self.portfolio = {}
    
    def purchase(self, instrument_id, quantity):

        purchase_price = self.watching[instrument_id].purchase(quantity)

        if instrument_id in self.portfolio and purchase_price != 0:
            self.portfolio[instrument_id] += quantity
            self.capital -= purchase_price * quantity

        elif self.watching.purchase != 0:
            self.portfolio[instrument_id] = quantity
            self.capital -= purchase_price * quantity

    def sell(self, instrument_id, quantity):

        #for the moment, only supports selling shares that are already owned

        sale_price = self.watching[instrument_id].sell(quantity)

        if sale_price != 0:
            self.portfolio[instrument_id] -= quantity
            self.capital += quantity * sale_price

    def evaluate(self, instrument_id):

        ret_percent = self.watching[instrument_id].get_dividend / self.watching[instrument_id].get_price

        instrument_risk = self.watching[instrument_id].get_risk

        if ret_percent > self.risk_func.calc_return(instrument_risk):
            self.purchase(instrument_id, 1)
        elif ret_percent < self.risk_func.calc_return(instrument_risk):
            self.sell(instrument_id, 1)


    def watch(self, instrument_id, server_url):
        s = xmlrpc.client.ServerProxy(server_url)
        self.watching[instrument_id] = s
        while True:
            self.evaluate(instrument_id)


    




        
