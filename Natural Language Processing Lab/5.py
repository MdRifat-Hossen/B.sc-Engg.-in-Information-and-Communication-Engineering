import subprocess,sys
for p in ["nltk"]:
    try:__import__(p)
    except:subprocess.check_call([sys.executable,"-m","pip","install",p])

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet

nltk.download('wordnet',quiet=True)
nltk.download('punkt',quiet=True)
nltk.download('punkt_tab',quiet=True)
nltk.download('averaged_perceptron_tagger_eng',quiet=True)

lemmatizer=WordNetLemmatizer()

text="Childrens are playing football happily."

words=word_tokenize(text)

pos_tags=pos_tag(words)

def get_wordnet_pos(tag):

    if tag.startswith('J'):
        return wordnet.ADJ
    
    elif tag.startswith('V'):
        return wordnet.VERB
    
    elif tag.startswith('N'):
        return wordnet.NOUN
    
    elif tag.startswith('R'):
        return wordnet.ADV
    
    else:
        return wordnet.NOUN

lemmatized=[
    lemmatizer.lemmatize(word,get_wordnet_pos(tag))
    for word,tag in pos_tags
]

print(lemmatized)