'''
Created on 17 May 2017

@author: Yukun
'''

import random

class ExecutionService(object):
    '''
    Base class for execution service. 
    Subclasses may be various types of simulator or live execution service.
    '''

    def no_operation(self, sym):
        raise NotImplemented
    
    def place(self, sym, side, quantity, price):
        '''
        place an order to execute.
        return (executed_price, executed_quantity)
        '''
        raise NotImplemented
    
    def amend(self, order):
        raise NotImplemented
    
    def cancel(self, order):
        raise NotImplemented
    
class SingleStockExecutionSimulator(ExecutionService):
    '''
    A simple execution simulator for trading a stock
    '''
        
    def __init__(self, sym, start, end, interval):
        self.marketprovider # create OHLCV provider
        
    def no_operation(self, sym):
        self.marketprovider.next()
        
    def place(self, sym, side, quantity, price):
        ohlcv = self.marketprovider.next()
        executed_price = (ohlcv[1] + ohlcv[2]) / 2 ## executed at the mid price of the day
        if (random.random() <= 0.9):
            executed_quantity = quantity
        else:
            executed_quantity = random.randint(round(quantity*0.8), quantity)
        return (executed_price, executed_quantity)
        
        