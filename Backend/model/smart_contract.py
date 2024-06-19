# @ Author: Bertan Berker
# @ File: smart_contract.py
# This is a file where I use the web3 library to interact with the smart contract and the ethereum blockchain for
# handling bets/payment between house and player

from web3 import Web3
import json


class Smart_Contract:
    def __init__(self):
        # Connect to Ganache
        ganache_url = "http://127.0.0.1:7545"
        web3 = Web3(Web3.HTTPProvider(ganache_url))

        print("Connection to Ganache successful?: " + str(web3.is_connected()))

        # Replace with the address of the deployed contract
        contract_address = '0x0f7A8B237eDF3fdf4558F9Be8770e4515Dd2D128'

        # Replace with the path to your contract's JSON file
        with open('../SmartContracts/build/contracts/Payments.json') as f:
            contract_json = json.load(f)
            contract_abi = contract_json['abi']

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)

        self.web3 = web3
        self.contract = contract
        self.house_balance = self.contract.functions.getHouseBalance().call()
        self.player_balance = self.contract.functions.getHouseBalance().call()
    
        # Set the default account (the first account in Ganache)
        self.web3.eth.default_account = self.web3.eth.accounts[0]

    def add_to_house(self, amount):
        tx_hash = self.contract.functions.addHouse(amount).transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Added to house balance:", amount)

    def add_to_player(self, amount):
        tx_hash = self.contract.functions.addPlayer(amount).transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Added to player balance:", amount)

    def sub_from_house(self, amount):
        tx_hash = self.contract.functions.subHouse(amount).transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Subtracted from house balance:", amount)

    def sub_from_player(self, amount):
        tx_hash = self.contract.functions.subPlayer(amount).transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Subtracted from player balance:", amount)

    def get_house_balance(self):
        balance = self.contract.functions.getHouseBalance().call()
        print("House balance:", balance)
        return balance

    def get_player_balance(self):
        balance = self.contract.functions.getPlayerBalance().call()
        print("Player balance:", balance)
        return balance

    def add_bet(self, amount):
        # Specify the from address when sending a transaction
        tx_hash = self.contract.functions.addBet(amount).transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Added bet:", amount)

    def zero_bet(self):
        tx_hash = self.contract.functions.zeroBet().transact({'from': self.web3.eth.default_account})
        self.web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Bet zeroed")
    
    def get_bet(self):        
        bet = self.contract.functions.getBet().call()
        print("Bet:", bet)
        return bet
