
from nltk.corpus import brown

# Print file ids of the brown corpus
print('File ids of brown corpus:')
print(brown.fileids())

# Select the first text (ca01) from the corpus
ca01 = brown.words('ca01')

# Display the words in ca01
print('\nca01 has following words:')
print(ca01)

# Count the total number of words in ca01
word_count = len(ca01)
print('\nca01 has', word_count, 'words')

# Print the categories or files in the brown corpus
print('\nCategories or files in brown corpus:')
print(brown.categories())

# Display statistics for each text in the brown corpus
print('\nStatistics for each text:')
print('AvgWordLen\tAvgSentenceLen\tno.ofTimesEachWordAppearsOnAvg\t\tFileName')

for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set(w.lower() for w in brown.words(fileid)))

    avg_word_len = num_chars / num_words
    avg_sent_len = num_words / num_sents
    avg_word_freq = num_words / num_vocab

    print(f"{int(avg_word_len)}\t\t\t{int(avg_sent_len)}\t\t\t{int(avg_word_freq)}\t\t\t{fileid}")
