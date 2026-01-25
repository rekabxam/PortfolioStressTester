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

            self._hist.loc[d, 'Return'] = round((self._hist['Close'].iloc[_]
                                                  - self._hist['Close'].iloc[_-1])
                                                  /self._hist['Close'].iloc[_-1], 3)
        
        return self._hist['Return']

class Portfolio():

    def __init__(self, value: int):

        self._value = value
        self._holdings = pd.DataFrame(data=[], columns=['Symbol', 'Category', 'Weighting'])
        self._holdings_added = 0
    
    def add_holding(self, info: list[str]):

        self._holdings = pd.concat([self._holdings, pd.DataFrame(data=[info], 
                                   columns=['Symbol', 'Category', 'Weighting'],
                                   index=[self._holdings_added])])
        self._holdings.reindex(index=range(len(self._holdings)))
        self._holdings_added += 1
    
    def calculate_returns(self):  # calculates return series of portfolio
        
        self._prices = pd.DataFrame(data=[])

    def calculate_specs(self):
        pass
        
class Simulation():
    pass

port = Portfolio(1)