from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# google play movie website
google_movie = "https://play.google.com/store/movies"
# Web Window
browser = webdriver.Chrome()
# Object of a mouse pointer
pointer = ActionChains(browser)
# Now browser project google play movie website
browser.get(google_movie)
browser.execute_script("window.scrollTo(0,900)")
enabling_btn = browser.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[3]/c-wiz/section/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/a')
pointer.move_to_element(enabling_btn).perform()
# Get Ranking Information
right_btn = browser.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[3]/c-wiz/section/div/div[3]/div/div/div/div[2]/button")
'''while True:
    right_btn.click()
    time.sleep(1)
    if len(browser.find_elements(By.XPATH,
                                 "//*[@id='yDmH0d']/c-wiz[2]/div/div/div[1]/c-wiz/div/c-wiz/c-wiz[3]/c-wiz/section/div/div[3]/div/div/div/div[3]")) == 0:
        break'''

soup = BeautifulSoup(browser.page_source, "lxml")
top_movies = soup.find_all("div", attrs={"class": "cXFu1"})
# with open("title.html", 'w', encoding="utf-8-sig") as log:
    # log.write(soup.prettify())
f = open("top_movies.csv", "w", encoding="utf-8-sig", newline='')
writer = csv.writer(f)

for row in top_movies:
    columns = row.find_all("div", attrs={"class": "ubGTjb"})
    data = [column.get_text() for column in columns]
    writer.writerow(data)

    #print(columns)
    #data = [column.get_text() for column in columns]

'''for index, top_movie in enumerate(top_movies):
    title = top_movie.find_next("span", attrs={"class": "DdYX5"}).get_text()
    rating = top_movie.find_all_next("span", attrs={"class": "w2kbF"})[0].get_text()
    genre = top_movie.find_all_next("span", attrs={"class": "w2kbF"})[1].get_text()
    review = top_movie.find_all_next("span", attrs={"class": "w2kbF"})[1].get_text()
    price = top_movie.find_next("span", attrs={"class": "w2kbF ePXqnb"}).get_text()
    print("Top {} : ".format(index+1)+title+" "+rating+" "+genre+" "+review+" "+price)
    with open("title.txt", "a", encoding="utf8") as f:
        f.write("Top {} : ".format(index+1)+title+" "+rating+" "+genre+" "+review+" "+price+"\n")'''