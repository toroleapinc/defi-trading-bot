"""Uniswap V2 interface."""
import json

# Uniswap V2 Router ABI (simplified)
ROUTER_ABI = json.loads('[{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"}]')

ROUTER_ADDRESS = '0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D'

class UniswapV2:
    def __init__(self, provider):
        self.provider = provider
        self.router = provider.w3.eth.contract(address=ROUTER_ADDRESS, abi=ROUTER_ABI)

    def get_price(self, token_in, token_out, amount_in):
        """Get swap output amount."""
        try:
            amounts = self.router.functions.getAmountsOut(amount_in, [token_in, token_out]).call()
            return amounts[-1]
        except Exception as e:
            print(f"Price query failed: {e}")
            return 0

    def swap(self, token_in, token_out, amount_in, min_out, deadline):
        """Execute a swap."""
        # simplified
        pass
