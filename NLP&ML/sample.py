import pandas
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import cross_val_score
from re import sub
from nltk.stem import PorterStemmer
print("******** setup **********")
stemmer = PorterStemmer()
cats = ['talk.politics.misc', 'sci.space']
newsgroups_train = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats)

print("******** prepare data **********")
new_data = []
for i in range(len(newsgroups_train.data)):
    new_data.append(sub("[^a-zA-Z]", " ", newsgroups_train.data[i]))

lowercase_data = []
for i in range(len(new_data)):
    lowercase_data.append(new_data[i].lower())

stemmed_data = []
for i in range(len(lowercase_data)):
    words = lowercase_data[i].split()
    stemmed_words = []
    for w in words:
        stemmed_words.append(stemmer.stem(w))
    stemmed_data.append(" ".join(stemmed_words))

print("******** setup vector model **********")
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer = "word", binary = True, min_df=2, stop_words='english')
docarray = vectorizer.fit_transform(stemmed_data).toarray()


print("******** model and XV **********")
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB(alpha=.01)

# do the 10-fold cross validation
scores = cross_val_score(model, docarray, newsgroups_train.target, cv=10)
print("Fold Accuracies: {}".format(scores))
print("XV Accuracy: {: 6.2f}".format(scores.mean()*100))
