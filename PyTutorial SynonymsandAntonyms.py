import nltk

from nltk.corpus import wordnet

synonyms = []

for syn in wordnet.synsets('computer'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)


antonyms = []

for syn  in wordnet.synset('small'):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

print(antonyms)




