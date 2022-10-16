import random
import math

class RiskFunction:

    a = 0
    b = 0
    c = 0
    func_type = 0

    def __init__(self):
        self.rand = random.randrange(10)

        if (self.rand < 3):
            #risk averse risk function, quadratic in nature
            self.func_type = 1
        elif (self.rand < 7):
            #risk neutral is linear
            self.func_type = 2
        else:
            #risk seeking is logarithmic
            self.func_type = 3
    
        self.a = random.randrange(10)
        self.b = random.randrange(10)
        self.c = random.randrange(10)

    def calc_return(self, risk_coeff):

        if (self.func_type == 1):
            return (risk_coeff**2) * self.a + self.b * risk_coeff + self.c

        elif (self.func_type == 2):
            return risk_coeff * self.a + self.b

        else:
            return math.log(risk_coeff) + self.a

        