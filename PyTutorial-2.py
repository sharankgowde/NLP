import nltk
nltk.download('stopwords')

text = """welcome you to programming knowledge. Lets start with our first tutorial on NLTK, We shall learn basic of NLTK here."""
demoWords = ["playing","happiness","going","doing","yes","no","I","having","had","haved"]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
#print(stop_words)


from nltk.tokenize import word_tokenize,sent_tokenize

tokenize_words = word_tokenize(text)

tokenize_words_without_stop_words=[]

for word in tokenize_words:
    if word not in stop_words:
        tokenize_words_without_stop_words.append(word)


print("Stop words which got removed",set(tokenize_words)-set(tokenize_words_without_stop_words))
print("Included all words including stop words",tokenize_words)
print("This is without stop words",tokenize_words_without_stop_words)



