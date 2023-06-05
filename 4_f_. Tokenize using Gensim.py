
#pip install gensim
from gensim.utils import tokenize

str = "I love to study Natural Language Processing in Python"
# tokenizing the text
# list(tokenize(str))

doc = tokenize(str)

tokens = [word for word in doc]
print(tokens)

