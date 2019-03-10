from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import openpyxl
from openpyxl import Workbook

browser = webdriver.Chrome("C:\\Users\\Srajika Gupta\\Downloads\\chromedriver_win32\\chromedriver.exe")


def search():
    username = input("Enter The name of user to be searched : ")
    url = 'https://github.com/' + username
    browser.get(url)

    repositories = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[2]/span')
    print("Number of Repositories : ", end=" ")
    print(repositories[0].text)

    projects = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[3]/span')
    print("Number of Projects : ", end=" ")
    print(projects[0].text)

    stars = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[4]/span')
    print("Stars : ", end=' ')
    print(stars[0].text)

    followers = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[5]/span')
    print("Followers : ", end=" ")
    print(followers[0].text)

    following = browser.find_elements_by_xpath('//*[@id="js-pjax-container"]/div/div[3]/div[2]/nav/a[6]/span')
    print("Following : ", end=" ")
    print(following[0].text)


search()