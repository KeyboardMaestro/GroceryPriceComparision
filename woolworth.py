import requests
from bs4 import BeautifulSoup

url = "https://www.woolworths.com.au/shop/browse/specials/half-price?icmpid=sm-hp-hero1:half-price-specials-nsw-vic%7Cwk32"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}
#Discount Page of Woolworth
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")