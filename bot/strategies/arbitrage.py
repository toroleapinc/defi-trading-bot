"""Cross-DEX arbitrage strategy."""
import logging

logger = logging.getLogger(__name__)

class ArbitrageStrategy:
    def __init__(self, dex_a, dex_b, min_profit_bps=30):
        self.dex_a = dex_a
        self.dex_b = dex_b
        self.min_profit_bps = min_profit_bps

    def find_opportunity(self, token_in, token_out, amount):
        """Check for price discrepancy between two DEXes."""
        price_a = self.dex_a.get_price(token_in, token_out, amount)
        price_b = self.dex_b.get_price(token_in, token_out, amount)

        if price_a == 0 or price_b == 0:
            return None

        # check both directions
        if price_a > price_b:
            profit_bps = (price_a - price_b) / price_b * 10000
            direction = 'buy_b_sell_a'
        else:
            profit_bps = (price_b - price_a) / price_a * 10000
            direction = 'buy_a_sell_b'

        if profit_bps >= self.min_profit_bps:
            logger.info(f"Arbitrage opportunity: {profit_bps:.1f} bps ({direction})")
            return {
                'direction': direction,
                'profit_bps': profit_bps,
                'price_a': price_a,
                'price_b': price_b,
            }
        return None

    def execute(self, opportunity, amount):
        """Execute the arbitrage trade."""
        # TODO: implement actual execution with gas estimation
        logger.info(f"Would execute: {opportunity}")
        pass
