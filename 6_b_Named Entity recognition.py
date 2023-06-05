
#pip install -U spacy
#python -m spacy download en_core_web_sm

import spacy
# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")
# Process whole documents
text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne."
doc = nlp(text)

entities = [(word.text, word.label_) for word in doc.ents]
print(entities)

# Analyse syntax
print("Noun phrases:", [word.text for word in doc.noun_chunks])
print("Verbs:", [word.text for word in doc if word.pos_ == "VERB"])

