import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(r"/Applications/code/cars2bot/chromedriver")


USERNAME = 'moviescriptbot'
PASSWORD = 'moviescriptbot2020'
LANDING_PAGE = 'https://www.instagram.com'

browser.get(LANDING_PAGE)
time.sleep(1)
browser.find_element_by_name("username").send_keys(USERNAME)
passwd_elem =  browser.find_element_by_name("password")
passwd_elem.send_keys(PASSWORD)
passwd_elem.submit() # logged in

time.sleep(2)

browser.get(post_link)
time.sleep(1)

sc = open('script_formatted.txt').read().split("\n")

def runtime():
    global sc
    count = 0
    for line in sc:
        if count%10==0 and not count==0:
            time.sleep(300)
        chars = list(line)
        for char in chars:
           elem = browser.find_element(By.CLASS_NAME, "Ypffh")
           time.sleep(random.uniform(0,0.1))
           elem.send_keys(char)
        elem.submit()
        time.sleep(10)
        count += 1
