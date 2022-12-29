"""
Quick program to test that market is functioning as it should. 

"""

HOST = "localhost"
PORT = 1026
BIDMSG = "b003100"
ASKMSG = ""

import socket
import threading as t
import time
import universe_params as p

def send_message(message1, message2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        print(s)

        s.connect((HOST, PORT))
        s.send(message1.encode())

        while (s.recv(7).decode() != "confirm"): 
            time.sleep(1)

        s.send(message2.encode())
        print("sent message")

        print(s.recv(30).decode())

        print("done sleeping")

        print(s.recv(30).decode())

        s.shutdown(socket.SHUT_RDWR)
        s.close()




def main():


    buyer_a = t.Thread(target=send_message, args=["s003000", "b003100"])
    seller_a = t.Thread(target=send_message, args=["s004000","a004099"])

    buyer_a.start()
    seller_a.start()


    

    return 0




if __name__ == "__main__":
    main()
