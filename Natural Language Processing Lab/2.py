import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.tokenize import sent_tokenize,word_tokenize

nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)

text="Hello world. This is an NLP course. It is very interesting!"

sentences=sent_tokenize(text)
words=word_tokenize(text)

print("Sentences:",sentences)
print("Words:",words)