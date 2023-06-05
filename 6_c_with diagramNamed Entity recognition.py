
# # nltk.download('treebank')
from nltk.corpus import treebank_chunk

# Retrieve the first tagged sentence
treebank_chunk.tagged_sents()[0]
# Retrieve the first chunked sentence
treebank_chunk.chunked_sents()[0]
# Draw the parse tree of the first chunked sentence
treebank_chunk.chunked_sents()[0].draw()
