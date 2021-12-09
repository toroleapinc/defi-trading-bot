"""Risk management and position limits."""
import logging

logger = logging.getLogger(__name__)

class RiskManager:
    def __init__(self, max_position_eth=1.0, max_slippage_bps=100, max_gas_gwei=200):
        self.max_position = max_position_eth
        self.max_slippage = max_slippage_bps
        self.max_gas = max_gas_gwei

    def check_trade(self, amount_eth, gas_price_gwei, expected_slippage_bps):
        """Check if a trade passes risk limits."""
        if amount_eth > self.max_position:
            logger.warning(f"Position too large: {amount_eth} ETH > {self.max_position}")
            return False
        if gas_price_gwei > self.max_gas:
            logger.warning(f"Gas too high: {gas_price_gwei} > {self.max_gas} gwei")
            return False
        if expected_slippage_bps > self.max_slippage:
            logger.warning(f"Slippage too high: {expected_slippage_bps} bps")
            return False
        return True

    def calculate_position_size(self, balance_eth, confidence):
        """Kelly-inspired position sizing."""
        # simplified kelly criterion
        fraction = min(confidence * 0.5, 0.25)  # never more than 25% of balance
        size = balance_eth * fraction
        return min(size, self.max_position)
