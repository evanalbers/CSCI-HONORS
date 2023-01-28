"""
Author: Evan Albers
Version Date: 29 December 2022
Summary: Class meant to represent portfolio of an agent, handles optimization, 
         weight calculation, etc.

"""

class Portfolio():

    def __init__(self):

        # maps instrument ids to a tuple containing four pieces of data: 
        # ER of asset, est. risk of asset, est. cov. w/ rest of portfolio, 
        # and weight of the asset within the portfolio
        self.assets = {}

        # the risk of the actual portfolio
        self.variance = 0

        # the expected return of the actual portfolio
        self.exp_ret = 0

    def calc_exp_ret(self):

        """ function to calculate expected return
    
            Simply sets expected return value of the actual portfolio

            Parameters
            ----------
            None

            Returns
            -------
            float 
                expected return of the actual portfolio
        """

        total = 0

        # for each asset in the actual portfolio
        for asset in self.assets:

            # calc its portion of exp_ret
            weight = self.assets[asset][3]
            exp_ret = self.assets[asset][0]
            total += weight * exp_ret
        
        # set and return
        self.exp_ret = total
        return self.exp_ret

    def calc_var(self, estimations):
        """ function to calculate standard deviation of actual portfolio
        
        Parameters
        --------
        estimations : dict
            a dict of estimations regarding the portfolio, including ER,
            pairwise covariances, etc. 

        Returns
        -------
        float
            standard deviation of the actual portfolio
        """

        variance = 0

        for id in estimations["variance"]:
            variance += (self.assets[id]["weight"]**2) * estimations["variance"][id]
        
        included = []
        for asset_one in estimations["covariance"]:
            for asset_two in estimations["covariance"][asset_one]:
                if asset_two not in included:
                    variance += 2 * self.assets[asset_one]["weight"] * \
                                self.assets[asset_two]["weight"] * \
                                estimations["covariance"][asset_one][asset_two]
                included.append(asset_two)

        self.variance = variance

        return self.variance

    def calc_optimum_weights(self, rfr):

        calculated = []
        
         

