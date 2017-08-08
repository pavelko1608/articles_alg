import requests
import pickle
from bs4 import BeautifulSoup
import sys
import newspaper
import time


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

sys.setrecursionlimit(10000)
#841 articles
def cnn_article():
	start_time = time.time()
	article_list = []
	cnn_paper = newspaper.build("http://edition.cnn.com/", memoize_articles=False)
	ctr = 0
	for article in cnn_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, 839, status = "Fetching CNN")
	with open('cnn_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('cnn_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("cnn len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"

#383 articles
def fox_article():
	start_time = time.time()
	article_list = []
	fox_paper = newspaper.build("http://nation.foxnews.com/", memoize_articles=False)
	ctr = 0
	for article in fox_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, 371, status = "Fetching Fox news")
	with open('fox_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('fox_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("fox len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"

cnn_article()
fox_article()
