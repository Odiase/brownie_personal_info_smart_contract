'''
This File Will read directly from the testnet(Goerli..etc)
and interact with the smart contract on these chains
'''
# third packages imports
from brownie import PersonalInfo, accounts, config

# local imports
from .extras import get_account



def read_contract():
    '''Gets Latest Contract Instance'''
    personal_info = PersonalInfo[-1]
    return personal_info

def view_favourite_number():
    # get contract
    contract = read_contract()

    return contract.view_favourite_number()


def change_number(number):
    # get contract and account
    account = get_account()
    contract = read_contract()

    # update number
    contract.change_favourite_number(number, {"from" : account})
    print("Updated!")


def create_person(name, phone_number, address):
    # get contract and account
    account = get_account()
    contract = read_contract()

    contract.create_person(name, int(phone_number), address, {"from" : account})
    print("Created!..")


def get_person_info(name):
    # getting contract
    contract = read_contract()

    return contract.get_person_info(name)


def delete_person(name):
    # getting contract
    account = get_account()
    contract = read_contract()

    contract.delete_person(name, {"from" : account})
    print("Deleted!...")

def main():
    run = True
    
    print("What Do you Want This Contract To Do For You: ")
    while True:
        answer = input("\n1. view favourite number \n2. Change Number \n3. Create A Person\n4. Get Person Info \n5.Delete A Person Info\n>> ")
        if answer == "q" or answer == "Q":
            break
        if answer == "1":
            print(view_favourite_number())
        elif answer == "2":
            new_number = int(input("Enter New Number: "))
            change_number(new_number)
        elif answer == "3":
            name = input("Name : ")
            phone_number = int(input("Phone Number: "))
            address = input("Address:  ")
            
            create_person(name, phone_number, address)
        elif answer == "4":
            name = input("Name : ")

            print(get_person_info(name))
        elif answer == "5":
            name = input("Name : ")

            delete_person(name)
