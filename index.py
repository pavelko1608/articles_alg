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

vox_data = []
with open('vox_articles.pkl', 'rb') as f:
		vox = pickle.load(f)
for article in vox:
	vox_data.append([0, article])

politico_data = []
with open('politico_articles.pkl', 'rb') as f:
		politico = pickle.load(f)
for article in politico:
	politico_data.append([0, article])

washington_post_data = []
with open('washington_post_articles.pkl', 'rb') as f:
		washington_post = pickle.load(f)
for article in washington_post:
	washington_post_data.append([0, article])		

left_wing_data = cnn_data + vox_data + politico_data + washington_post_data

fox_data = []
with open('fox_articles.pkl', 'rb') as f:
		fox = pickle.load(f)
for article in fox:
	fox_data.append([1, article])

observer_data = []
with open('observer_articles.pkl', 'rb') as f:
		observer = pickle.load(f)
for article in observer:
	observer_data.append([1, article])

breitbart_data = []
with open('breitbart_articles.pkl', 'rb') as f:
		breitbart = pickle.load(f)
for article in breitbart:
	breitbart_data.append([1, article])	

newsmax_data = []
with open('newsmax_articles.pkl', 'rb') as f:
		newsmax = pickle.load(f)
for article in newsmax:
	newsmax_data.append([1, article])				

right_wing_data = fox_data + observer_data + breitbart_data + newsmax_data

data = left_wing_data + right_wing_data
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
print "f1_score:", metrics.f1_score(labels_test, pred, average='micro')
print "recall_score:", metrics.recall_score(labels_test, pred, average='micro')
print "precision_score:", metrics.precision_score(labels_test, pred)
print "assessed correctly:", metrics.accuracy_score(labels_test, pred, normalize = False)
print "assessed incorrectly:", len(flat_test) - metrics.accuracy_score(labels_test, pred, normalize = False)
print "accuracy:", metrics.accuracy_score(labels_test, pred)

#     BEST SCORES
# Number of samples: 1124
# f1_score: 0.870996441281
# recall_score: 0.870996441281
# precision_score: 0.931034482759
# assessed correctly: 979
# assessed incorrectly: 145
# accuracy: 0.870996441281

