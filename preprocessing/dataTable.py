# -*- coding: utf-8 -*-
"""
Created on Wed May 25 18:14:35 2016

@author: Nguyen

Generates html table from a csv file in the current directory
"""

import pandas as pd

dataframe = pd.read_csv('../app/static/data/pivot/hybrid.csv')

table = dataframe.to_html(index=False)

with open("data.html", "w") as f:
    f.write(table.encode("UTF-8"))