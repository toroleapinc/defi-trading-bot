"""Gas price estimation."""

class GasEstimator:
    def __init__(self, provider):
        self.provider = provider
        self._history = []

    def estimate(self, speed='fast'):
        """Estimate gas price."""
        base = self.provider.gas_price
        multipliers = {'slow': 0.9, 'standard': 1.0, 'fast': 1.2, 'instant': 1.5}
        return int(base * multipliers.get(speed, 1.0))

    def is_profitable(self, expected_profit_wei, gas_limit, gas_price):
        """Check if trade is profitable after gas costs."""
        gas_cost = gas_limit * gas_price
        return expected_profit_wei > gas_cost * 1.5  # 50% margin
