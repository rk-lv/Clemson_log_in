from selenium import webdriver
import time
from username_passw import username, password
class bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.login_page = ""
    def login(self):
        page = self.driver.get("https://www.clemson.edu/canvas")
        button = self.driver.find_element_by_xpath("//*[@id=\"page\"]/div/div[1]/div/div[1]/div[1]/div/div/div[1]/a")
        button.click()
        time.sleep(3)
        login_window = self.driver.find_element_by_xpath("//*[@id=\"username\"]")
        login_window.send_keys(username)
        passw_window = self.driver.find_element_by_xpath("//*[@id=\"password\"]")
        passw_window.send_keys(password)
        time.sleep(3)
        duo_w = self.driver.find_element_by_xpath("//*[@id=\"submitButton\"]")
        duo_w.click()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id=\"duo_iframe\"]"))
        button = self.driver.find_element_by_xpath("//*[@id=\"auth_methods\"]/fieldset/div[1]/button")
        button.click()
    def close(self):
        self.driver.close()
C_bot = bot()
C_bot.login()
time.sleep(30)
C_bot.close()
