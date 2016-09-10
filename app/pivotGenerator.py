# Functions used to create pivot tables

import pandas as pd
import numpy as np

# Translates menu inputs into appropriate headings/functions
headings = {'total':'Total', 'hp':'HP', 'atk':'Attack', 'def':'Defense',
            'sp-atk':'Sp. Atk', 'sp-def':'Sp. Def', 'spd':'Speed',
            'gen':'Generation', 'ht':'Height', 'wt':'Weight', 'bmi':'BMI', 
            'type': 'Type'}
aggFuncs = {'count':np.count_nonzero, 'sum':np.sum, 'avg':np.mean, 
            'min':np.min, 'max':np.max, 'med':np.median}

# Generates a pivot table that works with HighCharts
def genTable(column, row, filter_val, aggregate, hybrid):
    if hybrid == "true":
        dataFrame = pd.read_csv('app/static/data/pivot/hybrid.csv')
    elif hybrid == "false":
        dataFrame = pd.read_csv('app/static/data/pivot/separate.csv')
        
    table = pd.pivot_table(dataFrame, values=headings[filter_val],
                index=headings[str(row)], columns=headings[str(column)], 
                           aggfunc=aggFuncs[aggregate])
    table = table.round(2)
    response = highchart_prep(table.to_csv())
    
    return (response)

# Converts a csv table into an output readable by HighCharts
def highchart_prep(csv):
    lines = csv.split('\n')
    header = True
    yLabels = []
    xLabels = []
    values = []
    xCount = 0
    for line in lines:
        items = line.split(',')
        if header:
            header = False
            for item in items[1:]:
                yLabels.append(item)
        else:
            xLabels.append(items[0])
            yCount = 0
            for item in items[1:]:
                try:
                    values.append([xCount, yCount, float(item)])
                except ValueError:
                    values.append([xCount, yCount, None])
                yCount += 1
            xCount += 1
    
    xLabels.pop()
    return (xLabels, yLabels, values)