# DeFi Trading Bot

Automated trading bot for decentralized exchanges (Uniswap V2/V3, PancakeSwap). Monitors mempool for arbitrage opportunities, executes swaps, and manages risk.

**⚠️ This is a research project. Use at your own risk. DeFi trading involves significant financial risk.**

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set environment variables:
```bash
export ETH_RPC_URL=https://mainnet.infura.io/v3/YOUR_KEY
export PRIVATE_KEY=your_wallet_private_key  # use a dedicated hot wallet
export BSC_RPC_URL=https://bsc-dataseed.binance.org/
```

3. Run:
```bash
python run_bot.py --strategy arbitrage --dex uniswap
```

## Strategies

- **Arbitrage**: Finds price differences between DEX pools and CEX reference prices
- **Sniper**: Monitors new token listings and buys early (very risky)
- **Liquidity**: Monitors large pool rebalances

## How It Works

The bot connects to an Ethereum/BSC node, subscribes to pending transactions in the mempool, decodes swap calls, and looks for profitable opportunities. When found, it submits a transaction with appropriate gas settings.

Risk management enforces max position size, slippage limits, and gas price caps.
