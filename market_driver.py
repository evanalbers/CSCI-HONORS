import sys
import marketserver as ms



def main():

    if len(sys.argv) != 4:
        print("usage: market_driver.py [instrument id] [maximum agent id length] [maximum instrument id length] [maximum price digits]")
        exit()
    elif not sys.argv[1].strip().isdigit() or not sys.argv[2].strip().isdigit() or not sys.argv[3].strip().isdigit():
        print("non-integer submitted by user")
        print("usage: market_driver.py [instrument id] [maximum agent id length] [maximum price digits]")

    market = ms.MarketServer(sys.argv[1], sys.argv[2], sys.argv[3])
    

if __name__ == "__main__":
    main()