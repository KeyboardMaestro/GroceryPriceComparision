from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
#options.add_argument("headless") # Using headless option to reduce memory usage.
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# options.add_argument("headless")
# add user Agent
browser = webdriver.Chrome(options=options)
#browser.find_element()

for page in range(1, 56):
    print("page : " + str(page))
    target_url = ("https://www.woolworths.com.au/shop/browse/specials/half-price?icmpid=sm-hp-hero2:half-price-specials%7Cwk33&pageNumber=" + str(page))
    browser.get(target_url)
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, "lxml")
    items = soup.find_all("section", attrs={"class": "product-tile-v2"}) # Find every block of an item.
    for item in items:
        title = item.find_next("a", attrs={"class":"product-title-link"}).get_text()
        price_check = item.find("div", attrs={"class" : "primary"})
        out_of_stock = item.find("div", attrs={"class":"product-tile-unavailable-tag ng-star-inserted"})
        if out_of_stock:
            print(title + " is " + "Out of stock")
            continue
        if price_check:
            price = price_check.get_text()
        print(title + " is " + price)
