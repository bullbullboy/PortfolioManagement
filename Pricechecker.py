#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

#const define
YahooFinanceURL = 'https://finance.yahoo.com/quote/{0}/?p={0}'
StockPriceClassName = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'

class PriceChecker:
    def fetchPrice(self, ticker):
        url = YahooFinanceURL.format(ticker)
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        stockPrice = soup.find(class_ = StockPriceClassName);
        return stockPrice.get_text()