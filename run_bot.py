"""Main bot entry point."""
import argparse
import asyncio
import logging
from bot.provider import BlockchainProvider
from bot.wallet import Wallet
from bot.dex.uniswap import UniswapV2
from bot.strategies.arbitrage import ArbitrageStrategy
from bot.risk import RiskManager
from bot.gas import GasEstimator

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger('bot')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--strategy', default='arbitrage', choices=['arbitrage', 'sniper'])
    parser.add_argument('--dex', default='uniswap', choices=['uniswap', 'pancakeswap'])
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    provider = BlockchainProvider()
    wallet = Wallet(provider)
    logger.info(f"Wallet: {wallet.address}, Balance: {wallet.balance_eth:.4f} ETH")

    risk = RiskManager()
    gas = GasEstimator(provider)

    if args.strategy == 'arbitrage':
        dex = UniswapV2(provider)
        # TODO: add second DEX for actual cross-dex arbitrage
        logger.info("Starting arbitrage bot...")
        logger.info("Monitoring mempool for opportunities...")
        # would run async loop here
    else:
        logger.info(f"Strategy {args.strategy} not fully implemented yet")

if __name__ == '__main__':
    main()
