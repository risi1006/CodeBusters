from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import openpyxl
from openpyxl import Workbook

browser = webdriver.Chrome('/home/risi/Downloads/chromedriver')


def opp():
    a = int(input(" 1.see your profile"
                  "2.search job oppourtunity"))
    if (a == 1):
        browser.get("https://www.linkedin.com")
        user = browser.find_element_by_name('session_key')

        # id1=input("enter ur user id")
        # psd=input("enter password")

        user.send_keys("risi1006@gmail.com")
        password = browser.find_element_by_id('login-password')
        password.send_keys("passofrj")
        password.send_keys(Keys.ENTER)
        search = browser.find_element_by_xpath('//*[@id="ember31"]/input')

        print(search)

    elif (a == 2):

        browser.get("https://www.linkedin.com")
        user = browser.find_element_by_name('session_key')

        # id1=input("enter ur user id")
        # psd=input("enter password")

        user.send_keys("risi1006@gmail.com")
        password = browser.find_element_by_id('login-password')
        password.send_keys("passofrj")
        password.send_keys(Keys.ENTER)
        search = browser.find_element_by_xpath('//*[@id="ember31"]/input')

        print(search)
        job = input("enter ur job criteria")
        job2 = browser.find_element_by_xpath('//*[@id="ember31"]/input')
        job2.send_keys(job)
        job2.send_keys(Keys.ENTER)

        pth = browser.find_elements_by_xpath('//*[@id="ember5"]/div[5]/div[2]/div/div[2]')
        print(pth)


opp()


