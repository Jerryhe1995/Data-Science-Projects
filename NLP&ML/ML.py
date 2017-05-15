import pandas as pd
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import cross_val_score
from re import sub
from nltk.stem import PorterStemmer

print("********** setup ***************")

stemmer = PorterStemmer()
# cats = ['talk.politics.misc','sci.space']
df= pd.read_csv('fake_or_real_news.csv')
print(df.dtypes)
newsgroups_train= df.iloc[:,2:]
print(newsgroups_train.shape)

# newsgroups_train = fetch_20newsgroups(subset = 'train', remove = ('headers','footers','quotes'), categories = cats)

print("******** prepare data***********")
new_data =dict()
for i in list(newsgroups_train):
    new_data[i] = []
    for j in newsgroups_train[i]:
        new_data[i].append(sub("[^a-zA-Z]"," ",j))
# print("Dtype of new_data" )
# print(newsgroups_train.dtypes)

lowercase_data = dict()
for i in list(new_data):
    lowercase_data[i]=[]
    for j in new_data[i]:
        lowercase_data[i].append(j.lower())
# print("The dtype fo lowercase_data")
# print(lowercase_data.dtypes)
# print("shape")
# print(lowercase_data.shape)

stemmed_data = dict()
for i in list(lowercase_data):
    stemmed_data[i]=[]
    for j in lowercase_data[i]:
        words = j.split()
        stemmed_words = []
        for w in words:
            stemmed_words.append(stemmer.stem(w))
        stemmed_data[i].append(" ".join(stemmed_words))
import numpy as np
import sklearn.datasets

examples = []
# examples.append(stemmed_data['title'])
examples.append(stemmed_data['text'])

target = []
target.append(stemmed_data['label'])
dataset = sklearn.datasets.base.Bunch(data=examples, target=target)

stemmed_data =dataset


print("********** setup vector model ************")
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(analyzer="word",binary=True, min_df= 1, stop_words="english")
docarry = vectorizer.fit_transform(stemmed_data).toarray()

#
# print("********* model and XV *************")
# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=4)
#
# #do the 10-fold cross validation
# scores = cross_val_score(model, docarry, newsgroups_train.target, cv=10)
# print("Fold Accuracies:{}".format(scores))
# print("XV Accuracy:{:6.2f}".format(scores.mean()*100))

# print("*********** setup vector model(naive bayes) ************")
# from sklearn.feature_extraction.text import CountVectorizer
# vectorizer = CountVectorizer(analyzer = "word", binary = True, min_df=2,stop_words='english')

print("*********** model and XV **************")
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB(alpha=0.1)

#do the 10-fold cross validation
scores = cross_val_score(model, docarry.reshape((2,1)), stemmed_data.target, cv=10 )
print("Fold Accuracies:{}".format(scores))
print("XV Accuracy: {: 6.2f}".format(scores.mean()*100))
