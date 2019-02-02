'''This script plots the sentiments using matlpolib'''

from sentiment_values_analyser import *

import matplotlib.pyplot as plt
 
# Data to plot

labels = 'Positive', 'Negative', 'Compund', 'Neutral'
sizes = [pos_value,neg_value,compound_value,neu_value]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.5, 0, 0, 0)  # explode 1st slice
 
#Plot
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")    
plt.axis('equal')
plt.show()
