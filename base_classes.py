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
                self._dates = list(self._dummy.calc_returns().index)

            elif self._min_date < self._dummy.get_min_date():
                self._min_date = self._dummy.get_min_date()
                self._dates = list(self._dummy.calc_returns().index)

    def calculate_returns(self): 
        
        self.get_hist_dates()
        self._prices = pd.DataFrame({"Date": self._dates, 
                                     "Value": [0 for _ in  range(len(self._dates))]}).set_index("Date")

        for _ in self._holdings.index:
            
            self._contrib = self._value * float(self._holdings.loc[_,'Weighting']) 
            self._dummy_df = Holding(*self._holdings.loc[_,['Symbol', 'Category']]).calc_returns().loc[self._min_date:] 

            for i,d in enumerate(self._dummy_df.index):
                
                if i != 0:
                    try:
                        self._contrib *= 1/self._dummy_df.iloc[i-1]
                    except RuntimeWarning:
                        pass
                
                self._prices.loc[d, 'Value'] += self._contrib
        
        return self._prices

    def calculate_specs(self):
        pass
        
class Simulation():
    pass

stock = Holding('XRO.AX', 'EQ')
port = Portfolio(500000)
port.add_holding(['CBA.AX','','0.2'])
port.add_holding(['XRO.AX','','0.2'])
print(port.calculate_returns())
