import random
import numpy as np
import pandas as pd
import yfinance as yf

class Holding():
    
    def __init__(self, ticker:  str, type: str, wgt: int):

        self._tkr = yf.Ticker(ticker)
        self._type = type
        self._wgt = wgt
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

    def get_weighting(self):
        return self._wgt

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
            self._dummy = Holding(*(self._holdings.loc[_,['Symbol', 'Category', 'Weighting']]))

            if _ == 0:
                self._min_date = self._dummy.get_min_date()
                self._dates = list(self._dummy.calc_returns().index)

            elif self._min_date < self._dummy.get_min_date():
                self._min_date = self._dummy.get_min_date()
                self._dates = list(self._dummy.calc_returns().index)

    def calculate_specs(self): 
        
        self.get_hist_dates()
        self._returns = pd.DataFrame({"Date": self._dates, 
                                     "Return": [np.float64(0) for _ in range(len(self._dates))]}).set_index("Date")

        for _ in self._holdings.index:
             
            self._holding = Holding(*self._holdings.loc[_,['Symbol', 'Category', 'Weighting']])

            for i,r in enumerate(
                self._holding.calc_returns().loc[self._min_date:]):

                self._returns.iloc[i] += np.float64(self._holding.get_weighting()) * r 

        self._specs = (np.mean(self._returns['Return']), 
                np.std(self._returns['Return']))

    def get_specs(self):        
        return self._specs
    
    def get_value(self):
        return self._value

class Simulation():
    
    def __init__(self, portfolio: Portfolio, n_pth: int, n_sim: int):

        self._port = portfolio
        self._n_pth, self._n_sim = n_pth, n_sim
 
    def calc_sim_price(self, price: float):
        return price + ((price * self._port.get_specs()[0]) +
                        (self._port.get_specs()[1]*random.random()))
    
    def gen_path(self):
        
        self._path = pd.DataFrame({"Sim Price": [self._port.get_value() for _ in range(self._n_pth+1)]},
                                  index=range(self._n_pth+1))
        self._port.calculate_specs()
        
        for _ in self._path.index:
            if _ != 0:
                self._path.loc[_] = self.calc_sim_price(self._path.loc[_-1])
        
        return self._path
        
    def gen_sim(self):
        pass

    def gen_summary(self):
        pass

port = Portfolio(100)
port.add_holding(['BHP.AX','','0.5'])
port.add_holding(['CBA.AX','','0.5'])
sim = Simulation(port,20,1)