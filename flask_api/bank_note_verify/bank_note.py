# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:15:58 2021

@author: satya
"""

from pydantic import BaseModel

#class for bank note measurement
class banknote(BaseModel):
    variance: float
    skewness: float
    curtosy: float
    entropy: float
    
    