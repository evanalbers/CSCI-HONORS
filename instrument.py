class Instrument:

    price = 0
    dividend = 0
    ret = 0
    risk = 0

    def __init__(self, price, dividend, id):
        self.price = price
        self.dividend = dividend 
        self.ret = price / dividend
        self.id = id

    def calculate_return(self):
        self.ret = self.price / self.dividend
    
    def set_price(self, price):
        self.price = price

    def set_dividend(self, dividend):
        self.dividend = dividend

    def set_risk(self, risk_multiple):
        self.risk = risk_multiple