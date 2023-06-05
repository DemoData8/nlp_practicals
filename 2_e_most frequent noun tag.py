import nltk
from collections import defaultdict

text = nltk.word_tokenize("Nick likes to play football. Nick does not like to play cricket.")
tagged = nltk.pos_tag(text)
print(tagged)

# Checking if it is a noun or not
addNounWords = []
count = 0
for word in tagged:
    val = tagged[count][1]
    if val == 'NN' or val == 'NNS' or val == 'NNPS' or val == 'NNP':
        addNounWords.append(tagged[count][0])
    count += 1

print(addNounWords)

temp = defaultdict(int)
# Memoizing count
for sub in addNounWords:
    for word in sub.split():
        temp[word] += 1

# Getting the word with the maximum frequency
res = max(temp, key=temp.get)

# Printing the result
print("Word with maximum frequency: " + str(res))
