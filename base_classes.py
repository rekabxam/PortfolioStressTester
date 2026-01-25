import numpy as np
import pandas as pd
import yfinance as yf

class Holding():
    
    def __init__(self, ticker:  str, type: str):

        self._tkr = ticker
        self._type = type
    
    def pull_prices(self):

        self._stock = yf.Ticker(self._tkr)
        self._hist = self._stock.history('max')

    def calc_returns(self):
        
        self.pull_prices()
        self._hist['Return'] = pd.NA

        for _, d in enumerate(self._hist.index):
            
            if _ == 0:
                pass

            self._hist.loc[d, 'Return'] = round((self._hist['Close'].iloc[_] - self._hist['Close'].iloc[_-1])/self._hist['Close'].iloc[_-1], 3)
        
        return self._hist['Return']

class Portfolio():
    pass

class Simulation():
    pass