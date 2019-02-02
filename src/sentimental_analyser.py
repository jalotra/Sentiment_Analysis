''' this function checks and describe the values to the 
        tweets text as positive ,negative or neutral.
        and their normalised values are given out'''

from main import *
import nltk
import pandas as pd
def analyser():
    nltk.download('vader_lexicon')
    list=[]
    object=SentimentIntensityAnalyzer()
    for index,rows in data.iterrows():
        list.append(object.polarity_scores(rows['tweets']))
    se=pd.Series(list)
    data['polarity']=se.values

    return data    
