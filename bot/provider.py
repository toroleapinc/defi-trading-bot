"""Blockchain connection and transaction helpers."""
import os
from web3 import Web3

class BlockchainProvider:
    def __init__(self, rpc_url=None, chain='ethereum'):
        self.rpc_url = rpc_url or os.environ.get('ETH_RPC_URL', '')
        self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
        self.chain = chain
        if not self.w3.is_connected():
            print(f"Warning: not connected to {chain} node")

    @property
    def gas_price(self):
        return self.w3.eth.gas_price

    def get_balance(self, address):
        return self.w3.eth.get_balance(address)

    def send_transaction(self, tx):
        signed = self.w3.eth.account.sign_transaction(tx, private_key=os.environ['PRIVATE_KEY'])
        return self.w3.eth.send_raw_transaction(signed.rawTransaction)
