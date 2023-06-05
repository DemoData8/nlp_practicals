
import nltk
from nltk import word_tokenize
from nltk import ChartParser


grammar1 = nltk.CFG.fromstring("""
S -> VP
VP -> VP NP
NP -> Det NP
Det -> 'that'
NP -> 'singular' Noun | 'flight'
VP -> 'Book'
""")

sentence = "Book that flight"

all_tokens = word_tokenize(sentence)

print(all_tokens)

ctr = ChartParser(grammar1)
parse = ctr.parse(all_tokens)
for tree in parse:
    print(tree)
    tree.draw()


# A context-free grammar (CFG) is a formal notation used to describe the syntax or structure of a language. It consists of a set of production rules that define how different components of the language can be combined to form valid sentences or phrases.