
from nltk.tokenize import RegexpTokenizer

str = "I love to study Natural Language Processing in Python"

# Use tokenize method
tokens = RegexpTokenizer('\s+', gaps = True).tokenize(str)
print(tokens)



# '\s+': This is the regular expression pattern passed as an argument to the RegexpTokenizer constructor. In this case, '\s+' matches one or more whitespace characters. The \s represents any whitespace character (spaces, tabs, newlines), and the + indicates that there can be one or more occurrences of the preceding pattern.

# gaps=True: This is an optional argument that is set to True. It tells the RegexpTokenizer to treat the regular expression pattern as gaps, meaning that the pattern will be used to identify token separators rather than token boundaries. In this case, the whitespace pattern '\s+' will be considered as token separators.