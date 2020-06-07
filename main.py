import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import re

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(3)

url = "https://www.starbucks.co.kr/menu/drink_list.do"
driver.get(url)

csv_filename = "StarbucksMenu.csv"
csv_open = open(csv_filename, "w+", encoding="utf-8")
csv_writer = csv.writer(csv_open)
csv_writer.writerow(("Menu", "Image"))

body = driver.find_element_by_css_selector("body")
for i in range(25):
	body.send_keys(Keys.PAGE_DOWN)
	time.sleep(1)

html = driver.page_source
bs = BeautifulSoup(html, "html.parser")
total_list = bs.find_all("li", {"class":re.compile("menuDataSet")})

for content in total_list:
	starbucks_menu = content.find("dd").text
	starbucks_img = content.find("img")["src"]
	csv_writer.writerow((starbucks_menu, starbucks_img))

driver.close()
