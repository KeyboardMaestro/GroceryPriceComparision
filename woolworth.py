from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
#options.add_argument("headless") # Using headless option to reduce memory usage.
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
# add user Agent
target_url = "https://www.woolworths.com.au/shop/browse/summer?pageNumber=1" # Summer Items Page of Woolworth

browser = webdriver.Chrome(options=options)
browser.get(target_url)

#browser.find_element(By.)

soup = BeautifulSoup(browser.page_source, "lxml")