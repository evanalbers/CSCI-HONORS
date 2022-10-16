class Bid:

    def __init__(self, instrument, bid_val, agent):
        self.instrument = instrument
        self.price = bid_val
        self.bidder = agent