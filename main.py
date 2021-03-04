import pandas as pd
from utils.log import logger
from binance_f import RequestClient
from binance_f.model import *
from binance_f.base.printobject import *
import json
import jsonpickle
from utils.config_reader import ConfigReader

config_reader = ConfigReader('config/api.ini')
api_key = config_reader.read_config('binance', 'api_key')
api_secret = config_reader.read_config('binance', 'api_secret')


def converter(obj):
    """
    转换api返回的json类对象格式，方便存储在本地
    :param obj:
    :return:
    """
    res = jsonpickle.encode(obj)
    res = json.loads(obj)
    return res


if __name__ == '__main__':
    logger.info('连接币安网站')
    request_client = RequestClient(api_key=api_key, secret_key=api_secret)

    logger.info('打印币种数据')
    symbols = request_client.get_exchange_information().symbols
    PrintMix.print_data(symbols)

    logger.info('保存K线数据')
    symbol = 'BTCUSDT'
    candlestick = request_client.get_candlestick_data(symbol=symbol, interval=CandlestickInterval.MIN1,
                                                      startTime=None, endTime=None, limit=10)
    candlestick = jsonpickle.encode(candlestick)
    candlestick = json.loads(candlestick)
    df = pd.DataFrame.from_dict(candlestick)
    df.to_csv('%s_ohlc.csv' % symbol)

