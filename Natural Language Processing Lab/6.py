import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)
nltk.download('averaged_perceptron_tagger_eng',quiet=True)

text="The cats are running and jumping quickly"

words=word_tokenize(text)

pos_tags=nltk.pos_tag(words)

print(pos_tags)