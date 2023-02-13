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
#options.add_argument("headless")
# options.add_argument("headless")
# add user Agent
browser = webdriver.Chrome(options=options)
#browser.find_element()
attributes = ["Date", "Price"]
index = 0
for page in range(1, 2): # 144
    print("page : " + str(page))
    target_url = ("https://www.coles.com.au/on-special?page=" + str(page))
    browser.get(target_url)
    #wait = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-121b1494-5 cbKguN coles-targeting-StylesCategoryStylesProductListContainer")))
    soup = BeautifulSoup(browser.page_source, "lxml")
    items = soup.find_all("section", attrs={"data-testid": "product-tile"}) # Find every block of an item
    for item in items:
        title = item.find("h2").get_text()
        price_check = item.find("span", attrs={"class": "price__value"})
        if not price_check:
            price = None
        else :
            price = price_check.get_text()
        index += 1
        row = [file_format, price]
        with open("./coles/"+str(index)+". "+title+".csv", "w", encoding="utf8") as record:
            writter = csv.writer(record)
            writter.writerow(attributes)
            writter.writerow(row)
