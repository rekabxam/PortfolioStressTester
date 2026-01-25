import numpy as np
import pandas as pd
import yfinance as yf

class Holding():
    
    def __init__(self, ticker:  str, type: str):

        self._tkr = ticker
        self._type = type
    
    def pull_prices(self):

        self._stock = yf.Ticker(self._tkr)
        self._hist = self._stock.history('max')['Close']
        
        return self._hist

    def calc_returns(self):
        pass


class Portfolio():
    pass

class Simulation():
    pass