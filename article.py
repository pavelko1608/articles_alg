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
		progress(ctr, len(cnn_paper.articles), status = "Fetching CNN")
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
		progress(ctr, len(fox_paper.articles), status = "Fetching Fox news")
	with open('fox_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('fox_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("fox len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"

#1666 articles
def vox_article():
	start_time = time.time()
	article_list = []
	vox_paper = newspaper.build("https://www.vox.com/", memoize_articles=False)
	ctr = 0
	for article in vox_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(vox_paper.articles), status = "Fetching VOX")
	with open('vox_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('vox_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("vox len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"

#81 article
def observer_article():
	start_time = time.time()
	article_list = []
	observer_paper = newspaper.build("http://observer.com/", memoize_articles=False)
	ctr = 0
	for article in observer_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(observer_paper.articles), status = "Fetching The New York Observer news")
	with open('observer_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('observer_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("observer len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"	

# cnn_article()
# fox_article()
# vox_article()
observer_article()