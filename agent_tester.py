"""A driver to debug and test agent implementation

Author: Evan Albers
Date: 8 November 2022

Test program to model a two agent system. Agents will have the following risk characteristics:

    - Risk function: ER - 

"""
import agent as a 

def main():

    agent_a = a.Agent()
    agent_a.watch(1)
    agent_b = a.Agent()
    agent_b.watch(1)


if __name__ == "__main__":
    main()