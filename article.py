import requests
import pickle
from bs4 import BeautifulSoup
import sys
import newspaper
import time

sys.setrecursionlimit(10000)
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
		print ctr
	with open('cnn_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('cnn_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("cnn len:")
	print len(newlist)
	elapsed_time = time.time() - start_time
	print elapsed_time, "seconds elapsed"

cnn_article()

