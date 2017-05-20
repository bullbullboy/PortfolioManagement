#!/usr/bin/env python
# -*- coding: utf-8 -*-

#for debug
#import pdb;
#pdb.set_trace()

import pandas as pd

class Portfolio:
    def __init__(self, srcCsvPath):
        self.df = pd.read_csv(srcCsvPath)
        #TODO:delete
        print(self.df)
        #example)print(self.df['Ticker'][0])