import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon',quiet=True)

sia=SentimentIntensityAnalyzer()

text="Today is Monday."

scores=sia.polarity_scores(text)

compound=scores['compound']

if compound>=0.05:
    sentiment="Positive"
elif compound<=-0.05:
    sentiment="Negative"
else:
    sentiment="Neutral"

print("Scores:",scores)
print("Overall Sentiment:",sentiment)