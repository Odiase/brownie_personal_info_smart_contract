from brownie import accounts, config, network

def get_account():
    '''Getting Account To Work With.'''

    if network.show_active() == True:
        return accounts[0]
    return accounts.add(config['wallets']['private_key'])