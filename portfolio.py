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
EXAMPLE = "example_data.json"

import json
import numpy as np
from numpy.linalg import inv
import universe_params as up

def getExpRetData(tickers):
    """
    Returns the expected return data associated with the given tickers 
    as a numpy array

    Parameters
    ----------
    tickers : list
        a list of numbers representing the index of sought after assets

    Returns
    -------
    exp_rets : nparray
        an array of the corresponding expected returns    
    """

    with open(EXAMPLE) as f:

        data = json.load(f)
    
    all_returns = data["mu"]
    ticker_list = data["asset_tickers"]

    # retrieve indices of tickers, append returns to list
    exp_ret = []
    for t in tickers:
        exp_ret.append(all_returns[t])

    return np.asarray(exp_ret)
    
def getRiskMatrix(tickers):
    """
    returns the risk matrix for given tickers
    
    Parameters
    ----------
    tickers : list
        list of ints representing indices of sought after assets
    
    Returns
    -------
    risk_matrix : nparray
        array of arrays, representing the variances, covariances of assets 
        detailed in ticker
    """

    # retrieving data
    with open(EXAMPLE) as f:

        data = json.load(f)

    all_asset_risk = data["variances"]
    matrix = []

    # subsetting overarching matrix
    for i in tickers:
        row = []
        for j in tickers:
            row.append(all_asset_risk[i][j])
        matrix.append(row)
    
    risk_matrix = np.array(matrix)

    return risk_matrix


def calculate_expected_return(weights):
    """
    Returns the expected return of the given portfolio weights

    Parameters
    ----------
    weights : nparray
        a 2D array in which the first row is the tickers, 2nd row is
        corresponding weight in the portfolio
    
    Returns
    -------
    expected return : float
        float representing the expected return of the portfolio
    """

    # tickers is a list of asset tickers in the portfolio as strings
    tickers = weights[0]

    exp_return_data = getExpRetData(tickers)

    expected_return = np.cross(weights, exp_return_data)

    return expected_return


def calculate_optimal_portfolio(tickers):
    """
    Returns a set of weights that represent the optimal portfolio weights for 
    the given asset

    Parameters
    ----------
    tickers : array of floats representing the tickers to be assessed

    Returns 
    -------
    weights : nparray
        a 2D array in which the first row is the tickers, 2nd row is
        corresponding weight in the portfolio
    """

    risk_matrix = getRiskMatrix(tickers)

    exp_return_data = getExpRetData(tickers)

    risk_free_vec = np.ones(exp_return_data.shape) * up.RFR

    numerator = np.matmul(inv(risk_matrix),(exp_return_data - risk_free_vec))

    denom = np.matmul(np.ones(risk_matrix.shape[0]).T, np.matmul(inv(risk_matrix),(exp_return_data - risk_free_vec)))

    t = numerator / denom

    return t
    
         

