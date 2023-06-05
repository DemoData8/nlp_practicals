
import nltk
from nltk.corpus import state_union
from nltk import sent_tokenize, word_tokenize
from nltk import pos_tag


# Create our training and testing data
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# Tokenize the sample text
tokenized_sentences = sent_tokenize(sample_text)

def process_content():
    for sentence in tokenized_sentences[:2]:
        words = word_tokenize(sentence)
        tagged = pos_tag(words)
        print(tagged)

process_content()
