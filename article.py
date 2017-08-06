import requests
import pickle
from bs4 import BeautifulSoup
import sys

sys.setrecursionlimit(10000)
def politico_article():
	rss_url_list = []
	url_list = []
	article_list = []

	rss_page = requests.get("http://www.politico.com/rss")
	rss_page_content = rss_page.content
	rss_page_soup = BeautifulSoup(rss_page_content, "lxml")
	generic_text_div = rss_page_soup.find("div", {"class": "generic-text"})
	rss_page_links = generic_text_div.findAll("a")
	for url in rss_page_links:
		if url.get("href"):
			link = url.get("href")
			rss_url_list.append(link)

	for url in rss_url_list:
		rss = requests.get(url) 
		rss_content = rss.content
		rss_soup = BeautifulSoup(rss_content, "lxml")
		items = rss_soup.findAll("item")
		for item in items:
			link = item.find("guid").text
			url_list.append(link)





	def getArticle(url):
	    result = requests.get(url)
	    c = result.content
	    soup = BeautifulSoup(c, "lxml")
	    text = ""
	    if(soup.find("div", {"class":"story-text"})):
	    	article = soup.find("div", {"class":"story-text"}).findAll('p')
	    	for element in article:
	        	text = text + " " + element.text + " "
	        article_list.append(text)	

	for url in url_list:
		getArticle(url)  

	with open('politico_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('politico_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)
	print("politico len:")
	print len(newlist)




def new_york_times_article():
	rss_url_list = []
	url_list = []
	shit_url_list = []
	article_list = []

	rss_page_1 = requests.get("http://rss.nytimes.com/services/xml/rss/nyt/US.xml")
	rss_page_content_1 = rss_page_1.content
	rss_page_2 = requests.get("http://rss.nytimes.com/services/xml/rss/nyt/Education.xml")
	rss_page_content_2 = rss_page_2.content
	rss_page_3 = requests.get("http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml")
	rss_page_content_3 = rss_page_3.content

	rss_page_soup_1 = BeautifulSoup(rss_page_content_1, "lxml")
	rss_page_soup_2 = BeautifulSoup(rss_page_content_2, "lxml")
	rss_page_soup_3 = BeautifulSoup(rss_page_content_3, "lxml")

	generic_text_div_1 = rss_page_soup_1.findAll("guid")
	generic_text_div_2 = rss_page_soup_2.findAll("guid")
	generic_text_div_3 = rss_page_soup_3.findAll("guid")

	rss_page_links_1 = generic_text_div_1
	for url in rss_page_links_1:
		link = url.contents
		shit_url_list.append(link)
	rss_page_links_2 = generic_text_div_2
	for url in rss_page_links_2:
		link = url.contents
		shit_url_list.append(link)
	rss_page_links_3 = generic_text_div_3
	for url in rss_page_links_3:
		link = url.contents
		shit_url_list.append(link)

	for sublist in shit_url_list:
		for item in sublist:
			url_list.append(item)			

	def getArticle(url):
	    result = requests.get(url)
	    c = result.content
	    soup = BeautifulSoup(c, "lxml")
	    
	    if(soup.find("p", {"class":"story-body-text" or "story-content"})):
	    	for a in soup.find_all('a'):
    			a.extract()
	    	article = soup.findAll("p", {"class":"story-body-text" or "story-content"})
	    	for element in article:
	    		for sub_element in element.contents:
	        		article_list.append(sub_element)	

	for url in url_list:
		getArticle(url)  

	with open('nyt_articles.pkl', 'wb') as f:
		pickle.dump(article_list, f)

	with open('nyt_articles.pkl', 'rb') as f:
		newlist = pickle.load(f)

	print("nyt length: ")	
	print len(newlist)
	
politico_article()
new_york_times_article()
