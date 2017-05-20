#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PriceChecker
import Portfolio

# main-routine

# user define
ownTickerList = ['XOM', 'KO', 'PG', 'MO', 'GIS', 'VZ']
benchmarkTickerList = ['HDV', 'VTI', 'VT', 'VYM']
tickerList = ownTickerList + benchmarkTickerList

portfolio = Portfolio.Portfolio('asset.csv')
checker = PriceChecker.PriceChecker()

for ticker in tickerList:
    print(ticker + " : " + checker.fetchPrice(ticker))
