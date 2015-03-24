import requests
from bs4 import BeautifulSoup
import unicodedata


url="http://liverpoolfc.com/news/latest"

r=requests.get(url)

soup=BeautifulSoup(r.content)

oae=soup.find_all("div",{"class":"boxNewsTypeContent"})[0]

for link in oae.find_all("div",{"class":"SearchResult"}):
	news=link.find_all("div",{"class":"SearchDetails MoreResults"})[0]
	print str(news.h1.a.text)
	print unicodedata.normalize('NFKD', news.p.text).encode('ascii','ignore')   
	 