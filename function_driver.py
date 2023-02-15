"""
Quick file to run tests on random functions
"""

import portfolio as p

def main():

    t = p.calculate_optimal_portfolio([0,1,2])
    print(t)

if __name__ == '__main__':
    main()