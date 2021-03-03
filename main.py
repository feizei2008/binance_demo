import pandas as pd
import numpy as np
from utils.config_reader import ConfigReader

config_reader = ConfigReader('config/api.ini')
token = config_reader.read_config('binance', 'api_key')

