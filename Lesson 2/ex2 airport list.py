# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 12:15:45 2014

@author: changli
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html)
        airport_list = soup.find(id = "AirportList")
        for option in airport_list.find_all('option'):
            if "All" not in option['value']:
                data.append(option['value'])
    print data
    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()