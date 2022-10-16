class Ask:

    def __init__(self, instrument, ask_val, agent):
        self.instrument = instrument
        self.price = ask_val
        self.bidder = agent