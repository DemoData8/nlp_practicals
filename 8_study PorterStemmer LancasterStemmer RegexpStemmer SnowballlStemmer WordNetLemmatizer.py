
# PorterStemmer
print("<============================= PorterStemmer =============================>")
from nltk import PorterStemmer
word_stemmer = PorterStemmer()
print(word_stemmer.stem('writing'))

#LancasterStemmer
print("<============================= LancasterStemmer =============================>")
import nltk
from nltk import LancasterStemmer
Lanc_stemmer = LancasterStemmer()
print(Lanc_stemmer.stem('writing'))

#RegexpStemmer
print("<============================= RegexpStemmer =============================>")
import nltk
from nltk import RegexpStemmer
Reg_stemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
print(Reg_stemmer.stem('writing'))

#SnowballStemmer
print("<============================= SnowballStemmer =============================>")
import nltk
from nltk import SnowballStemmer
english_stemmer = SnowballStemmer('english')
print(english_stemmer.stem ('writing'))

#WordNetLemmatizer
print("<============================= WordNetLemmatizer =============================>")
from nltk import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print("word :\tlemma")
print("rocks :", lemmatizer.lemmatize("rocks"))
print("corpora :", lemmatizer.lemmatize("corpora"))
# a denotes adjective in "pos"
print("better :", lemmatizer.lemmatize("better", pos ="a"))



