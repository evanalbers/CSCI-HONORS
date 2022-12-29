import universe_params as p

class Bid:

    def __init__(self, agent, bid_val):
        self.price = bid_val
        self.bidder = agent

    @classmethod
    def fromString(cls, bid_string):
        
        return cls(bid_string[1:1+p.MAX_AGENT_ID_LENGTH], 
                   int(bid_string[1+p.MAX_AGENT_ID_LENGTH:1+p.MAX_AGENT_ID_LENGTH+p.MAX_PRICE_DIGITS]))

    def toString(self):
        return "bid value: " + str(self.price) + "\n"+ "bidder: " + self.bidder + "\n"
