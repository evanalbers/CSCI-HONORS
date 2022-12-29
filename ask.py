import universe_params as p

class Ask:

    def __init__(self, agent, price):

        self.price = price
        self.seller = agent

    
    @classmethod
    def fromString(cls, ask_string):
        return cls(ask_string[1:1+p.MAX_AGENT_ID_LENGTH], 
                   int(ask_string[1+p.MAX_AGENT_ID_LENGTH:1+p.MAX_AGENT_ID_LENGTH+p.MAX_PRICE_DIGITS]))

    def toString(self):
        return "ask value: " + str(self.price) + "\n"+ "bidder: " + self.seller + "\n"