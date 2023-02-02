import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EA%B0%90%EC%9E%90&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15"}
res = requests.get(url, headers=headers)
print(res.status_code)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
print(res.text)

potatoes = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(potatoes[0].find("div", attrs={"class":"name"}))