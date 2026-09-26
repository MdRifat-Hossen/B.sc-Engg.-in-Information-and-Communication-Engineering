import subprocess,sys
try:import string
except:subprocess.check_call([sys.executable,"-m","pip","install","string"])

text="Hello, World! This is Natural Language Processing."
cleaned=text.lower().translate(str.maketrans('','',string.punctuation))
print(cleaned)