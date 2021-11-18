"""PancakeSwap (BSC) interface."""
ROUTER_ADDRESS = '0x10ED43C718714eb63d5aA57B78B54704E256024E'

class PancakeSwap:
    def __init__(self, provider):
        self.provider = provider
        # Similar to Uniswap but on BSC

    def get_price(self, token_in, token_out, amount_in):
        # same interface, different router
        pass

    def swap(self, token_in, token_out, amount_in, min_out, deadline):
        pass
