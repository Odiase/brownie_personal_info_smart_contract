'''
This File Will read directly from the testnet(Goerli..etc)
and interact with the smart contract on these chains
'''

from brownie import PersonalInfo, accounts, config

def read_contract():
    '''Interacting with a smart contract using the abi and the address'''
    personal_info = PersonalInfo[-1]


def main():
    read_contract()