# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import pos_tag
from nltk import chunk

para = "Hello! My name is Gufran Qureshi. Today you'll be learning NLTK."

# sentence tokenization
sents = sent_tokenize(para)
print("\nsentence tokenization\n===================\n", sents)

# word tokenization
print("\nword tokenization\n===================\n")
words = [word_tokenize(sent) for sent in sents]

print(words)

# POS Tagging
tagged_words = [pos_tag(sent_words) for sent_words in words]
print("\nPOS Tagging\n===========\n", tagged_words)

# Chunking
tree = [chunk.ne_chunk(tagged_sent) for tagged_sent in tagged_words]
print("\nchunking\n========\n")
print(tree)

# involves grouping words together into meaningful chunks based on their part-of-speech tags. The goal of chunking is to identify and extract specific information or patterns from sentences.

# In chunking, a chunk refers to a sequence of words that form a meaningful unit, such as a noun phrase (NP), verb phrase (VP), or prepositional phrase (PP). By identifying these chunks, we can gain insights into the syntactic structure of a sentence and extract useful information.

# The cat is running
#  the cat = noun phrase
#  is running = verb phrase
# (S
#   (NP The/DT cat/NN)
#   is/VBZ
#   (VP running/VBG)
#   ./.)