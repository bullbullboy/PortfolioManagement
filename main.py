#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PriceChecker

# main-routine

# user define
ownTickerList = ['XOM', 'KO', 'PG', 'MO', 'GIS', 'VZ']
benchmarkTickerList = ['HDV', 'VTI', 'VT', 'VYM']

tickerList = ownTickerList + benchmarkTickerList

#printout ticker and stock price
checker = PriceChecker.PriceChecker()
for ticker in tickerList:
    print(ticker + " : " + checker.fetchPrice(ticker))
