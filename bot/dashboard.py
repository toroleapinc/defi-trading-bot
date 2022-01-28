"""Simple monitoring dashboard (WIP)."""
# TODO: add flask dashboard for monitoring trades
# For now just log to file
import json
import os
from datetime import datetime

LOG_FILE = 'logs/trades.jsonl'

def log_trade(trade_data):
    os.makedirs('logs', exist_ok=True)
    trade_data['timestamp'] = datetime.utcnow().isoformat()
    with open(LOG_FILE, 'a') as f:
        f.write(json.dumps(trade_data) + '\n')
