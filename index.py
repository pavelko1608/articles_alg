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
	President Trump and his lawyers have discussed whether he could pardon his relatives and aides to undercut, or even end, the special counsel’s investigation into charges that his campaign colluded with Russia to influence the 2016 election, The Washington Post reported on Thursday night.

There’s no question that with a stroke of his pen, Mr. Trump can shield his son Donald Trump Jr., his son-in-law, Jared Kushner, and other close associates from potential prosecution. Despite the uproar that would set off, we know by now that Mr. Trump loves the grand gesture, whatever the consequences. Besides, his family is at stake.

While his authority to pardon is crystal clear, a crucial, threatening, legal ambiguity should make him think twice about using this authority.

The Constitution gives the president “power to grant reprieves and pardons for offenses against the United States, except in cases of impeachment.” The framers had sound reasons for bestowing that authority. As Alexander Hamilton explained, criminal law in the late 18th century was so severe that without the pardon power to soften it, “justice would wear a countenance too sanguinary and cruel.”

Consistent with the framers’ design, the Supreme Court has interpreted the president’s pardon power broadly. The president can pardon anyone for any crime at any time — even before a suspect has been charged. Congress cannot withdraw presidential pardons, and prosecutors and courts cannot ignore them.

Continue reading the main story
But could a pardon be a criminal abuse of power? Some would argue that would contradict the founders’ vision of unlimited pardon authority. If a president sold pardons for cash, though, that would violate the federal bribery statute. And if a president can be prosecuted for exchanging pardons for bribes, then it follows that the broad and unreviewable nature of the pardon power does not shield the president from criminal liability for abusing it.

The Justice Department and the F.B.I. proceeded on this premise in 2001 when they opened an investigation into possible bribery charges arising out of President Bill Clinton’s pardon of the fugitive financier Marc Rich, whose former wife had donated $450,000 to Clinton’s presidential library. The investigation lasted until 2005, though no charges resulted.
Of course, bribery would not be the relevant crime. No one thinks that Donald Jr. or Jared Kushner — or anyone else involved in the Russia scandal — would pay the president for a pardon.

Yet federal obstruction statutes say that a person commits a crime when he “corruptly” impedes a court or agency proceeding. If it could be shown that President Trump pardoned his family members and close aides to cover up possible crimes, then that could be seen as acting “corruptly” and he could be charged with obstruction of justice. If, as some commentators believe, a sitting president cannot be indicted, Mr. Trump could still face prosecution after he leaves the White House.

There is strong support for the claim that the obstruction statutes apply to the president.

In 1974, when the House Judiciary Committee voted to impeach President Richard Nixon, members on both sides of the debate acknowledged that presidential obstruction of justice was not only impeachable but also criminal. A quarter century later, the Senate split 50-50 on whether to remove President Clinton from office on obstruction charges, but senators from both parties agreed that the obstruction laws applied to the president.

There is a broad consensus that a president exercises the pardon power properly — not “corruptly” — when he grants clemency based on considerations of mercy or the public welfare. President Gerald Ford invoked both of those values when he pardoned Nixon: He said that a prosecution of the former president would be too divisive and that Nixon had suffered enough. President George H.W. Bush gestured to both values when he pardoned former Reagan administration officials for their involvement in the Iran-contra scandal.

In Trump’s case, the question would be whether he was acting out of the goodness of his heart, or covering up for his family, his associates and himself.

We expect — and hope — that prosecutors and courts would give wide latitude to a president in evaluating his pardon decisions. Only in the most egregious cases should a president face criminal liability for actions taken while in office.

While the law on this subject is unsettled, that in itself should be unsettling to the president as he considers whether to grant clemency. Not only might the pardons constitute obstruction, but the pardoned individuals might be compelled to testify against Mr. Trump without any recourse to the Fifth Amendment right against self-incrimination, since they would no longer have any concern about incriminating themselves.

He could ensure that his family members and aides get off scot-free for any crimes they may have committed during the 2016 campaign. But by extricating those individuals from a legal predicament, he might make his own predicament worse.
"""]
trump_vector = vectorizer.transform(trump_article)
pred2 = clf.predict(trump_vector)
print pred2




