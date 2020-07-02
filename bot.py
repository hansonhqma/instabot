from selenium import webdriver
from selenium.webdriver.common.by import By

class bot:
    def __init__(self, USERNAME, PASSWORD):
        if not (isinstance(USERNAME, str) and isinstance(PASSWORD, str)):
            print("Invalid username/password type")
            return
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.landing_page = r'https://www.instagram.com'

    def comment(self, text, link):
        if not (isinstance(text, str) and isinstance(link, str)):
            print("Invalid text or link type")
            return
        if text=='':
            print("Emtpy text field")
            return

        if not 'instagram.com' in link.lower():
            print("Not an Instagram link")

