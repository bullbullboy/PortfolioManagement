# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

#user define
tickerList = ['XOM', 'KO', 'PG', 'MO', 'GIS']

#const define
YahooFinanceURL = 'https://finance.yahoo.com/quote/{0}/?p={0}'
StockPriceClassName = 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'

#printout ticker and stock price
for ticker in tickerList:
    url = YahooFinanceURL.format(ticker)
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    stockPrice = soup.find(class_ = StockPriceClassName);
    print(ticker + " : " + stockPrice.get_text())