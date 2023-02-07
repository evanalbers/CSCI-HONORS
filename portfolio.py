"""
Author: Evan Albers
Version Date: 29 December 2022
Summary: series of functions to aid with portfolio calculation, to isolate
         and help with debugging

         Notes: 

         - portfolio weights should be stored as a 2d array, 1st row is
         the ticker of the asset, 2nd is the weight in the portfolio, 
         can be negative, allowing for short selling

         - should store tickers in alphabetical order, keep it consistent
         They will be mapped to floats on such a basis, very important to
         avoid confusion


"""

import numpy as np
import universe_params as up

def calculate_expected_return(weights):
    """
    Returns the expected return of the given portfolio weights

    Params
    --------
    weights : nparray
        a 2D array in which the first row is the tickers, 2nd row is
        corresponding weight in the portfolio
    
    Returns
    --------
    expected return : float
        float representing the expected return of the portfolio
    """

    tickers = weights[0]

    exp_return_data = getExpRetData(tickers)

    expected_return = np.cross(weights, exp_return_data)

    return expected_return


def calculate_optimal_portfolio(tickers):
    """
    Returns a set of weights that represent the optimal portfolio weights for 
    the given asset

    Params
    --------
    tickers : array of floats representing the tickers to be assessed

    Returns 
    --------
    weights : nparray
        a 2D array in which the first row is the tickers, 2nd row is
        corresponding weight in the portfolio
    """

    risk_matrix = getRiskMatrix(tickers)

    exp_return_data = getExpRetData(tickers)

    risk_free_vec = np.ones(exp_return_data.shape) * up.RFR

    



    





















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
        
         

