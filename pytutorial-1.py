import nltk
import matplotlib.pyplot as plt



text = """welcome you to programming knowledge. Lets start with our first tutorial on NLTK, We shall learn basic of NLTK here."""

from nltk.tokenize import word_tokenize

word_tokenize=word_tokenize(text)

#print(word_tokenize(text))


#from nltk.tokenize import sent_tokenize
#print(sent_tokenize(text))

from nltk.probability import FreqDist

fd = FreqDist(word_tokenize)
print(fd.most_common(3))

fd.plot(30, cumulative=False)
plt.show()
