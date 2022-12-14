#stlib imports
import time

# third packages imports
from brownie import accounts, config, PersonalInfo, network

# local imports
from .extras import get_account



def deploy_personal_info():
    '''Deploying Contract'''

    account = get_account()
    publish_source = config['environments'][network.show_active()].get('verify')

    # deploying the smart contract
    personal_info = PersonalInfo.deploy({"from" : account}, publish_source=publish_source)

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