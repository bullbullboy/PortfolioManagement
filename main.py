#!/usr/bin/env python
# -*- coding: utf-8 -*-

import StockPricechecker

# main-routine

# user define
ownTickerList = ['XOM', 'KO', 'PG', 'MO', 'GIS', 'VZ']
benchmarkTickerList = ['HDV', 'VTI', 'VT', 'VYM']

tickerList = ownTickerList + benchmarkTickerList

#printout ticker and stock price
for ticker in tickerList:
    scraper = StockPricechecker.StockPriceChecker()
    print(ticker + " : " + scraper.fetchPrice(ticker))
