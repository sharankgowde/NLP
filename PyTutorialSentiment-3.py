import nltk
nltk.download('wordnet')
nltk.download('vader_lexicon')

from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = """welcome you to programming knowledge. Lets start with our first tutorial on NLTK, We shall learn basic of NLTK here."""
demoWords = ["playing","happiness","going","doing","yes","no","I","having","had","haved"]


lemmatizer = WordNetLemmatizer()
stemmer =PorterStemmer()

for word in demoWords:
    print("Word:", word)
    print("stemmer:",stemmer.stem(word))
    print("lemmatizer:", lemmatizer.lemmatize(word,"v"))


sai = SentimentIntensityAnalyzer()
print (sai.polarity_scores("this is not good at all"))

