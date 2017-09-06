# coding: utf-8
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pickle
from nltk.stem.snowball import SnowballStemmer
from feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split 
import time

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

vectorizer = TfidfVectorizer(strip_accents = "unicode", lowercase = False)
vectors = vectorizer.fit_transform(flat_train)
vectors_test = vectorizer.transform(flat_test)

# clf = MultinomialNB(alpha=.01, fit_prior = False)
# clf.fit(vectors, labels_train)
# pred = clf.predict(vectors_test)

# from sklearn import tree
# clf = tree.DecisionTreeClassifier(min_samples_split = 1)
# clf = clf.fit(vectors, labels_train)
# pred = clf.predict(vectors_test)
t0 = time.time()
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(alpha = .001)
clf.fit(vectors, labels_train)
pred = clf.predict(vectors_test)

print "Number of samples:", len(flat_test)
print "f1_score:", metrics.f1_score(labels_test, pred, average='micro')
print "recall_score:", metrics.recall_score(labels_test, pred, average='micro')
print "precision_score:", metrics.precision_score(labels_test, pred)
print "assessed correctly:", metrics.accuracy_score(labels_test, pred, normalize = False)
print "assessed incorrectly:", len(flat_test) - metrics.accuracy_score(labels_test, pred, normalize = False)
print "accuracy:", metrics.accuracy_score(labels_test, pred)
print (time.time() - t0) / 60, "mins elapsed"
#     BEST SCORES
# Number of samples: 1306
# f1_score: 0.914241960184
# recall_score: 0.914241960184
# precision_score: 0.896103896104
# assessed correctly: 1194
# assessed incorrectly: 112
# accuracy: 0.914241960184
# 6.14256568352 mins elapsed


trump_article = ["""
	Published August 30, 2017
 
NOW PLAYING
Trump: We will lower taxes for middle-income Americans
Close
President Trump called Wednesday for drastically simplifying the tax code, formally kicking off his push for comprehensive tax reform and offering a preview of the hardball politics he'll employ as he tries to muscle it through.  

“I don't want to be disappointed by Congress,” Trump said in Springfield, Mo. “Do you understand me?” 

The president wasted little time applying direct pressure to Missouri's Democratic senator, Claire McCaskill, during his visit to her state.  

“We must lower our taxes,” Trump said. “And your senator Claire McCaskill, she must do this for you and if she doesn't do it for you, you have to vote her out of office.”
Trump rallied supporters as he tries to bring tax reform to the front of the agenda for Congress, as lawmakers return from the August recess next week. He called this a “once-in-a-generation opportunity to deliver real tax reform for everyday hard-working Americans.”

The White House has not yet released a detailed tax reform plan. But describing his principles for reform, Trump called for a code that is “simple, fair, and easy to understand.”

“This enormous complexity is very unfair," the president said. "It disadvantages ordinary Americans who don’t have an army of accountants while benefiting deep-pocketed special interests."
The president delivered the speech at the Loren Cook Company, a local business that manufactures fans, blowers, vents and laboratory exhaust systems.

Trump quipped that his proposal to do away with loopholes may not be preferable to wealthy people like him and the owner of the Loren Cook Company, but portrayed it as the right thing to do for workers.

TRUMP LOOKING TO COHN, MNUCHIN TO SELL TAX PLAN

“And I’m speaking against myself when I do this, I have to tell you," he said. "And I might be speaking against Mr. Cook. And we’re both OK with it. Is that right? It’s crazy. Maybe we shouldn't be doing this, you know. But we’re doing the right thing.”
The president also said he’d like to “ideally” bring the corporate tax rate down to 15 percent from 35 percent, saying it would “make us highly competitive.”

Campaign politics also hovered over the visit, as displayed by Trump's shot at McCaskill -- an endangered Democrat up for re-election next year.

By expressing optimism Congress would pass a tax bill, Trump alluded to the Senate’s inability to pass legislation to repeal and replace President Obama’s health care law.

“I think Congress is going to make a comeback,” Trump said. “I hope so. I tell you what, the United States is counting on it.”

Ahead of the speech, a White House spokesman said Springfield was chosen as the backdrop for Trump’s speech because it is “the birthplace of America’s Main Street, Route 66.”

The aide said the purpose of the speech was for the president to speak to the American people about “why tax reform and relief is needed to unrig the system and jumpstart our economy.”

Some of the president’s Cabinet members and aides traveled with the president to Springfield on Wednesday, including Treasury Secretary Steven Mnuchin, Commerce Secretary Wilbur Ross, Director of the National Economic Council Gary Cohn and Small Business Administrator Linda McMahon.

A number of Missouri Republicans also attended the speech, including Sen. Roy Blunt, Gov. Eric Greitens, Lt. Gov. Mike Parson and members of the state’s congressional delegation.

Ahead of the president’s speech Wednesday, Democratic Senate leader Chuck Schumer called for Democrats and Republicans working together to “craft a bipartisan package that’s good for the American people.”

“Rather than writing a partisan bill that will benefit the wealthy and special interests, they should commit to working with Democrats, through regular order, to craft a bill in the light of day that puts the middle class and those struggling to make it first,” Schumer said in a Wednesday call with reporters.
"""]
trump_vector = vectorizer.transform(trump_article)
pred2 = clf.predict(trump_vector)
print pred2




