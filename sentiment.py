#import nltk

#nltk.download('vader_lexicon')

#from nltk.sentiment.vader import SentimentIntensityAnalyser
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

#sid = SentimentIntensityAnalyser()

a = "I am Samyak"


print(sid.polarity_scores(a))
