import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
import re
from selenium import webdriver as wd


url = " https://www.youtube.com/playlist?list=PLW_uvsSPliju_CkrMa0GEcCMs_4AYC_Ym"
driver = wd.Chrome(executable_path="chromedriver.exe")
driver.get(url)
last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source
driver.close()

soup = BeautifulSoup(html_source)
youtube_title= soup.select(' #video-title')
youtube_url= soup.select( '#content > a')

f = open("popeTV.md", mode='w+', encoding='utf8')
for i  in range(528) :
    f.write( "# [" + youtube_title[i].text.strip() + "](https://www.youtube.com" + youtube_url[i]['href']+")\n\n\n")
f.close()
