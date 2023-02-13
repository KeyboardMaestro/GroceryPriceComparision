import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

date = datetime.datetime.now()
file_format = date.strftime("%d%m%y")
options = webdriver.ChromeOptions()
#options.add_argument("headless") # Using headless option to reduce memory usage.
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# options.add_argument("headless")
# add user Agent
browser = webdriver.Chrome(options=options)
#browser.find_element()
index = 0
for page in range(1, 56):
    print("page : " + str(page))
    target_url = ("https://www.woolworths.com.au/shop/browse/specials/half-price?icmpid=sm-hp-hero2:half-price-specials%7Cwk33&pageNumber=" + str(page))
    browser.get(target_url)
    wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "product-tile-v2")))
    soup = BeautifulSoup(browser.page_source, "lxml")
    items = soup.find_all("section", attrs={"class": "product-tile-v2"}) # Find every block of an item
    for item in items:
        index += 1
        title = item.find_next("a", attrs={"class":"product-title-link"}).get_text()
        title = title.replace("/", ",")
        price_check = item.find("div", attrs={"class" : "primary"})
        out_of_stock = item.find("div", attrs={"class":"product-tile-unavailable-tag ng-star-inserted"})
        if price_check:
            price = price_check.get_text()
        if out_of_stock:
            price = None
        row = [file_format, price]
        with open("./items/"+str(index)+". "+title+".csv", "a", encoding="utf8") as record:
            writter = csv.writer(record)
            writter.writerow(row)