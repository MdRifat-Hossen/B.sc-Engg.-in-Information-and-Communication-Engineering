import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)

ps=PorterStemmer()

text="The cats are running and jumping quickly."

words=word_tokenize(text)

stemmed=[ps.stem(w) for w in words]

print(stemmed)