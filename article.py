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
#852 articles
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

#395 articles
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

#1673 articles
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

#87 article
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

# 210 articles
def breitbart_article():
	start_time = time.time()
	article_list = []
	breitbart_paper = newspaper.build("http://www.breitbart.com/", memoize_articles=False)
	ctr = 0
	for article in breitbart_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(breitbart_paper.articles), status = "Fetching the Breitbart news")
	with open('breitbart_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('breitbart_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("breitbart len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"	

#381 articles
def newsmax_article():
	start_time = time.time()
	article_list = []
	newsmax_paper = newspaper.build("http://www.newsmax.com/", memoize_articles=False)
	ctr = 0
	for article in newsmax_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(newsmax_paper.articles), status = "Fetching the NewsMax news")
	with open('newsmax_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('newsmax_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("newsmax len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"

#209 articles
def politico_article():
	start_time = time.time()
	article_list = []
	politico_paper = newspaper.build("http://www.politico.com/", memoize_articles=False)
	ctr = 0
	for article in politico_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(politico_paper.articles), status = "Fetching the Politico news")
	with open('politico_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('politico_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("politico len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"	

#207 articles
def washington_post_article():
	start_time = time.time()
	article_list = []
	washington_post_paper = newspaper.build("http://www.politico.com/", memoize_articles=False)
	ctr = 0
	for article in washington_post_paper.articles:
		article.download()
		article.parse()
		article_list.append(article.text)
		ctr += 1
		progress(ctr, len(washington_post_paper.articles), status = "Fetching the Washington Post news")
	with open('washington_post_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('washington_post_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("washington_post len:")
	print len(newlist)
	elapsed_time = (time.time() - start_time) / 60
	print elapsed_time, "minutes elapsed"										

cnn_article()
fox_article()
vox_article()
observer_article()
breitbart_article()
newsmax_article()
politico_article()
washington_post_article()