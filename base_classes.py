import numpy as np
import pandas as pd
import yfinance as yf

class Holding():
    
    def __init__(self, ticker:  str, type: str):

        self._tkr = yf.Ticker(ticker)
        self._type = type
        self._hist = self._tkr.history('max')
    
    def calc_returns(self):
        
        self._hist['Return'] = pd.NA

        for _, d in enumerate(self._hist.index):
            if _ == 0:
                pass
            self._hist.loc[d, 'Return'] = round((self._hist['Close'].iloc[_]
                                                  - self._hist['Close'].iloc[_-1])
                                                  /self._hist['Close'].iloc[_-1], 3)
        
        return self._hist['Return']
    
    def get_min_date(self):
        return min(self._hist.index)

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
    
    def get_hist_dates(self):
        
        for _ in self._holdings.index:
            self._dummy = Holding(*(self._holdings.loc[_,['Symbol', 'Category']]))

            if _ == 0:
                self._min_date = self._dummy.get_min_date()
                self._dates =self._dummy.calc_returns().index

            elif self._min_date < self._dummy.get_min_date():
                self._dates = self._dummy.calc_returns().index
        
        return self._dates

    def calculate_returns(self): 
        pass
        #prices df that sets index as dates and columns (use get_hist_dates)

    def calculate_specs(self):
        pass
        
class Simulation():
    pass

stock = Holding('XRO.AX', 'EQ')
port = Portfolio(1)
port.add_holding(['CBA.AX','',''])
port.add_holding(['XRO.AX','',''])
print(port.get_hist_dates())
print(stock.get_min_date())