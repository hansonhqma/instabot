from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class bot:
    def __init__(self, USERNAME, PASSWORD):
        if not (isinstance(USERNAME, str) and isinstance(PASSWORD, str)):
            print("Invalid username/password type")
            return
        self.USERNAME = USERNAME
        self.PASSWORD = PASSWORD
        self.landing_page = r'https://www.instagram.com'
        self.browser = webdriver.Chrome('DRIVERS/chromedriver')
        try:
            self.browser.get(self.landing_page)
            time.sleep(3)
            self.browser.find_element_by_name("username").send_keys(self.USERNAME)
            PWD_ELEM = self.browser.find_element_by_name("password")
            PWD_ELEM.send_keys(self.PASSWORD)
            PWD_ELEM.submit()
        except Exception as e:
            print("Error logging into account:", e)

    def comment(self, text, link):
        if not (isinstance(text, str) and isinstance(link, str)):
            print("Invalid text or link type")
            return
        if text=='':
            print("Emtpy text field")
            return

        if not 'instagram.com' in link.lower():
            print("Not an Instagram link")
            return
        try:
            self.browser.get(link)
        except Exception as e:
            print("Unable to access post:", e)
            return
        try:
            COMMENT_BOX = self.browser.find_element(By.CLASS_NAME, "Ypffh") # finish here
        except Exception as e:
            print("Error accessing comment section:", e)
            return
        try:
            COMMENT_BOX.send_keys(text)
        except Exception as e:
            print("Error sending text to comment field:", e)
            return
        try:
            COMMENT_BOX.submit()
        except Exception as e:
            print("Error submitting text:", e)
            return
