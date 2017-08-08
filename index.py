from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pickle
from nltk.stem.snowball import SnowballStemmer
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split

cnn_data = []
with open('cnn_articles.pkl', 'rb') as f:
		cnn = pickle.load(f)
for article in cnn:
	cnn_data.append([0, article])


fox_data = []
with open('fox_articles.pkl', 'rb') as f:
		fox = pickle.load(f)
for article in fox:
	fox_data.append([1, article])

data = cnn_data + fox_data
labels, articles = targetFeatureSplit(data)
articles_train, articles_test, labels_train, labels_test = train_test_split(articles, labels, test_size = 0.3, random_state = 42)

flat_train = []
flat_test = []
for sublist in articles_train:
    for article in sublist:
        flat_train.append(article)
for sublist in articles_test:
    for article in sublist:
        flat_test.append(article)  

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(flat_train)
vectors_test = vectorizer.transform(flat_test)

clf = MultinomialNB(alpha=.01)
clf.fit(vectors, labels_train)
pred = clf.predict(vectors_test)

print "Number of samples:", len(flat_test)
print "f1_score:", metrics.f1_score(labels_test, pred, average='macro')
print "recall_score:", metrics.recall_score(labels_test, pred, average='macro')
print "precision_score:", metrics.precision_score(labels_test, pred)
print "accuracy_score:", metrics.accuracy_score(labels_test, pred, normalize = False)

#     BEST SCORES
# Number of samples: 368
# f1_score: 0.828246753247
# recall_score: 0.795156695157
# precision_score: 0.955882352941
# accuracy_score: 322

