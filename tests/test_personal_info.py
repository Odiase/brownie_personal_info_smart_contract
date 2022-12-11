from brownie import PersonalInfo, accounts

# TESTS are Seperated Into Three Categories, Namely:
# Arrange
# Act
# Assert


def test_deploy():
    # Arrange (all th epieces we need to setup)
    account = accounts[0] 
    personal_info = PersonalInfo.deploy({"from" : account})

    # Act (We are going to carry out actions---here it i sdeploying the smart contract)
    default_favourite_num = personal_info.view_favourite_number()
    expected_default_favourite_num = 0

    # Assert
    assert expected_default_favourite_num == default_favourite_num
    

def test_update_favourite_number():
    # Arrange
    account = accounts[0]
    personal_info = PersonalInfo.deploy({"from" : account})

    #assert
    expected_number = 8
    transaction = personal_info.change_favourite_number(8, {"from" : account})
    transaction.wait(1)
    updated_number = personal_info.view_favourite_number()
    assert updated_number == expected_number
