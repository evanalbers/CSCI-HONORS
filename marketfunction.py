"""
AUTHOR: EVAN ALBERS
PURPOSE: Code that actually executes the operation of the server, listening for bids, 
asks, etc

"""
import universe_params as p
from ask import Ask
from bid import Bid

def read(agent_socket, serv):

    msg = agent_socket.recv(p.MAX_AGENT_ID_LENGTH + p.MAX_PRICE_DIGITS + 1).decode()
    print(msg)
   
    if len(msg) == 0:
        agent_socket.close()
        return False

    elif msg and (msg[0] == "s"):
        #make sure not in current list of connections, then add new agent 
        if msg[1:p.MAX_AGENT_ID_LENGTH+1] not in serv.connections:
            serv.connections[msg[1:p.MAX_AGENT_ID_LENGTH+1]] = agent_socket
            agent_socket.send("confirm".encode())

    elif msg and (msg[0] == "b"):
        serv.submitBid(Bid.fromString(msg))
        agent_socket.send("confirm".encode())
        serv.checkMatch()


    elif msg and (msg[0] == "a"):
        serv.submitAsk(Ask.fromString(msg))
        agent_socket.send("confirm".encode())
        serv.checkMatch()    

    elif msg and (msg[0] == 'p'):
        agent_socket.send(str(serv.price).encode())

    return True

def handleAgent(agent_socket, serv):

    cond = True
    while(cond):

        cond = read(agent_socket, serv)


