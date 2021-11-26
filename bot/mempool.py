"""Monitor pending transactions in mempool."""
import asyncio
import json
from web3 import Web3

# Common DEX function signatures
SWAP_SIGNATURES = {
    '0x38ed1739': 'swapExactTokensForTokens',
    '0x8803dbee': 'swapTokensForExactTokens',
    '0x7ff36ab5': 'swapExactETHForTokens',
    '0x18cbafe5': 'swapExactTokensForETH',
}

class MempoolMonitor:
    def __init__(self, provider, callback=None):
        self.w3 = provider.w3
        self.callback = callback

    async def watch_pending(self):
        """Watch for pending swap transactions."""
        pending_filter = self.w3.eth.filter('pending')
        while True:
            try:
                txs = pending_filter.get_new_entries()
                for tx_hash in txs:
                    try:
                        tx = self.w3.eth.get_transaction(tx_hash)
                        if tx and tx.input[:10] in SWAP_SIGNATURES:
                            if self.callback:
                                self.callback(tx)
                    except Exception:
                        pass
            except Exception as e:
                print(f"Mempool error: {e}")
            await asyncio.sleep(0.1)
