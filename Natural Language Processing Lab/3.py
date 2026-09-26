import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords',quiet=True)
nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)

text="This is a simple sentence for removing stopwords in NLP."

words=word_tokenize(text)

stop_words=set(stopwords.words('english'))

filtered=[w for w in words if w.lower() not in stop_words]

print(filtered)