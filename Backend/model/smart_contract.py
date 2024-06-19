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

        print("Connection to Ganache successful?: " + str(web3.isConnected()))

        # Replace with the address of the deployed contract
        contract_address = '0xYourContractAddress'

        # Replace with the path to your contract's JSON file
        with open('../../SmartContracts/build/contracts/Payments.json') as f:
            contract_json = json.load(f)
            contract_abi = contract_json['abi']

        contract = web3.eth.contract(address=contract_address, abi=contract_abi)

        self.web3 = web3
        self.contract = contract
        self.house_balance = self.contract.functions.getHouseBalance().call()
        self.player_balance = self.contract.functions.getHouseBalance().call()

    def add_to_house(self, amount):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.addHouse(amount).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.house_balance = self.contract.functions.getHouseBalance().call()
        print(f"Updated House Balance: {self.house_balance}")


    def add_to_player(self, amount):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.addPlayer(amount).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.player_balance = self.contract.functions.getPlayerBalance().call()
        print(f"Updated Player Balance: {self.player_balance}")

    def get_house_balance(self):
        return self.house_balance

    def get_player_balance(self):
        return self.house_balance

    def sub_from_house(self, amount):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.subHouse(amount).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.house_balance = self.contract.functions.getHouseBalance().call()
        print(f"Updated House Balance: {self.house_balance}")

    def sub_from_player(self, amount):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.subPlayer(amount).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.player_balance = self.contract.functions.getPlayerBalance().call()
        print(f"Updated Player Balance: {self.player_balance}")

    def add_bet(self, amount):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.addBet(amount).buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.player_bet = self.contract.functions.getPlayerBet().call()
        print(f"Updated Player Bet: {self.player_bet}")

    def zero_bet(self):
        account = self.web3.eth.accounts[0]
        transaction = self.contract.functions.zeroBet().buildTransaction({
            'from': account,
            'nonce': self.web3.eth.getTransactionCount(account)
        })
        signed_tx = self.web3.eth.account.signTransaction(transaction, private_key='0xYourPrivateKey')
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        self.player_bet = self.contract.functions.getBet().call()
        print(f"Player Bet Reset: {self.player_bet}")

    def get_bet(self):
        return self.contract.functions.getBet().call()