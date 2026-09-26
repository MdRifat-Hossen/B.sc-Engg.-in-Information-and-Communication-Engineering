import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)

text="NLP is fun. NLP is interesting. NLP helps in many applications."

words=word_tokenize(text)

fdist=FreqDist(words)

print(fdist.most_common(6))