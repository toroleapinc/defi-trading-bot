"""Wallet and account management."""
import os
from web3 import Web3

class Wallet:
    def __init__(self, provider):
        self.provider = provider
        self.private_key = os.environ.get('PRIVATE_KEY', '')
        if self.private_key:
            self.account = provider.w3.eth.account.from_key(self.private_key)
            self.address = self.account.address
        else:
            self.address = None

    @property
    def balance_eth(self):
        if not self.address: return 0
        return self.provider.get_balance(self.address) / 1e18

    def approve_token(self, token_address, spender, amount):
        """Approve ERC20 token spending."""
        # simplified - would need actual ABI
        contract = self.provider.w3.eth.contract(address=token_address)
        tx = contract.functions.approve(spender, amount).build_transaction({
            'from': self.address,
            'nonce': self.provider.w3.eth.get_transaction_count(self.address),
        })
        return self.provider.send_transaction(tx)
