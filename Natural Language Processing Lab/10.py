import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag,ne_chunk

nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)
nltk.download('averaged_perceptron_tagger_eng',quiet=True)
nltk.download('maxent_ne_chunker_tab',quiet=True)
nltk.download('words',quiet=True)

text="Messi was born in Hawaii and worked at Microsoft."

words=word_tokenize(text)

pos_tags=pos_tag(words)

ner_tree=ne_chunk(pos_tags)

print(ner_tree)