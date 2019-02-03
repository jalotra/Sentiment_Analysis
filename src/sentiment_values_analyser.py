'''This script analyses the maximum of Positive Neutral Negative and Compound among each tweet '''
from sentimental_analyser import *
from main import *

data=analyser()
pos_value=0
neg_value=0
compound_value=0
neu_value=0 
keys=['pos','neg','compound','neu']
for rows in data['polarity']:
    result=max(rows, key=rows.get)
    if result==keys[0]:
        pos_value +=1
    elif result==keys[1]:
        neg_value += 1
    elif result==keys[2]:
        compound_value += 1
    else:
        neu_value += 1
                 
             
