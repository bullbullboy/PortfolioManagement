#!/usr/bin/env python
# -*- coding: utf-8 -*-

class PFAnalyzer:
    def __init__(self, portfolio):
        self.portfolio = portfolio

    def showPriceList(self):
        tickerList = self.portfolio.getTickerList();
        for ticker in tickerList:
            print(ticker + ":" + self.portfolio.priceOf(ticker))
        
