import json
import threading
import time
from datetime import datetime
# https://stackoverflow.com/questions/62580240/django-cannot-import-name-config-from-decouple
from decouple import config
from models.price import Price


class Strategy(object):
    price: Price

    def __init__(self, exchange, interval=60, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.next_call = time.time()
        self.portfolio = {}
        self.exchange = exchange
        # Load account portfolio for pair at load
        self.get_portfolio()

    def _run(self):
        self.is_running = False
        self.start()
        self.run(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            print(datetime.now())
            if self._timer is None:
                self.next_call = time.time()
            else:
                self.next_call += self.interval

            self._timer = threading.Timer(self.next_call - time.time(), self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

    def get_portfolio(self):
        self.portfolio = {'currency': self.exchange.get_asset_balance(self.exchange.currency),
                          'asset': self.exchange.get_asset_balance(self.exchange.asset)}

    def get_price(self):
        try:
            self.price = self.exchange.symbol_ticker()
        except Exception as e:
            pass


