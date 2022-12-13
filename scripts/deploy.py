# third packages imports
from brownie import accounts, config, PersonalInfo, network
import time



def get_account():
    '''Getting Account To Work With.'''

    if network.show_active() == True:
        return accounts[0]
        # getting my connected blockchain network
    return accounts.add(config['wallets']['private_key'])


def deploy_personal_info():
    '''Deploying Contract'''

    # getting private key from .yaml file
    # account = accounts.add(config['wallets']['from_key'])

    account = get_account()
    # deploying the smart contract
    personal_info = PersonalInfo.deploy({"from" : account})

    # sleeping for a second so as to avoid a brownie exception that says the web3 connection was closed too soon(It's a bug in brownie)
    time.sleep(1)

    # creating a new user with the smart contract
    create_person_transaction = personal_info.create_person("Efosa", 2349020705214, "Ikorodu, Lagos, Nigeria", {"from" : account})

    # waiting for a second for the transaction to go through
    create_person_transaction.wait(1)

    # calling the get person function in the contract
    person_created = personal_info.get_person_info('Efosa')



def main():
    deploy_personal_info()