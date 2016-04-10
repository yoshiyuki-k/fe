# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 10:42:57 2015

@author: yoshiyuki
"""
import math

class BlackScholes:
    """ hogehoge """
    
    def __init__(self):
        self.name = "foo"
        
        
    def calc_d1(self, forward, strike, maturity, sigma):
        return (math.log(forward / strike) + 0.5 * sigma * sigma * maturity) / \
        (sigma * math.sqrt(maturity))
        
    
    def calc_d2(self, forward, strike, maturity, sigma):
        return (math.log(forward / strike) - 0.5 * sigma * sigma * maturity) \
        / (sigma * math.sqrt(maturity))
        

    def calc_price(self, forward, strike, maturity, sigma):
        return forward * self.calc_d1(forward, strike, maturity, sigma) - \
        strike * BlackScholes.calc_d2(forward, strike, maturity, sigma)
        
    
def func():
    print(math.log(2))
    a = BlackScholes()
    print(a.calc_price(1,1,1,0.2))
    


        
        