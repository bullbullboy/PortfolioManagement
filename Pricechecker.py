#!/usr/bin/env python
# -*- coding: utf-8 -*-

#for debug
#import pdb;
#pdb.set_trace()

from urllib.request import urlopen
from bs4 import BeautifulSoup

#const define
YahooFinanceURL = 'https://finance.yahoo.com/quote/{0}/?p={0}'
StockPriceClassName = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'

class PriceChecker:
    def __init__(self):
        self.priceDictionary=dict()
        
    def fetchPrice(self, ticker):
        if ticker in self.priceDictionary:
            return self.priceDictionary[ticker]
        else:
            url = YahooFinanceURL.format(ticker)
            html = urlopen(url)
            soup = BeautifulSoup(html, "html.parser")
            stockPrice = soup.find(class_ = StockPriceClassName);
            self.priceDictionary[ticker] = stockPrice.get_text()
            return stockPrice.get_text()