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
        
        
    def calc_d1(self, sigma, maturity, forward, strike):
        return (math.log(forward / strike) + 0.5 * sigma * sigma * maturity) \
        / (sigma * math.sqrt(maturity))
        




        
        