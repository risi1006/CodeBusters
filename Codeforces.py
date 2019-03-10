from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import openpyxl
from openpyxl import Workbook
browser = webdriver.Chrome('/home/risi/Downloads/chromedriver')



def profile():
    a=int(input("1 : See your profile\n"
            "2 : See others profile..(handle needed)\n"
            "3 : Search for a question and Friend's solution \n"
            "4 : Upcoming Contest \n"
            "5 : Running Contest --> "))
    if a==1:
        browser.get('https://codeforces.com/profile/')
        rating = browser.find_element_by_class_name('user-cyan')
        contri = browser.find_elements_by_xpath('//*[@id="sidebar"]/div[2]/div[4]/div[2]/ul[1]/li[2]/span')

    elif a==2:
        handle=input("Enter the handle of the user --> ")
        url="https://codeforces.com/profile/"+str(handle)
        browser.get(url)
        rating = browser.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div[2]/ul/li[1]/span[1]')
        contri = browser.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div[2]/ul/li[2]/span')
        print("Rating : ",end="")
        print(rating.text)
        print("Contribution : ",end="")
        print(contri[0].text)
    elif a==3:
        #id = input("User id : ")
        #password = input("your password : ")

        problem = input("Enter a problem no or Problem name : ")
        browser.get('https://codeforces.com')



        pset = browser.find_element_by_xpath('//*[@id="body"]/div[3]/div[5]/ul/li[5]/a')
        pset.click()
        b = browser.find_element_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div/img')
        b.click()
        elem1 = browser.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/div[5]/div/span[2]/input')
        elem1[0].send_keys(problem)

        ex = browser.find_elements_by_xpath('//*[@id="pageContent"]/div[2]')



        #question details
        detail = ex[0].text
        ques = detail[41:45]  #question id
        div = detail[45]      #question division

        #url for friend standing for an specific topic
        url = "https://codeforces.com/problemset/status/"+str(ques)+"/problem/"+str(div)+"?friends=on"

        browser.get(url)

        #user login
        a = browser.find_element_by_xpath('//*[@id="header"]/div[2]/div[2]/a[1]')
        a.click()

        id1 = browser.find_element_by_id('handleOrEmail')
        id1.send_keys('royal_risi')

        psd = browser.find_element_by_id('password')
        psd.send_keys('passofrj')
        psd.send_keys(Keys.ENTER)

        time.sleep(10)

        #printing the deatil of friends
        for i in range(120):
            print("-",end="")
        elem5 = browser.find_elements_by_xpath('//*[@id="pageContent"]/div[4]')
        print(elem5[0].text)
        for i in range(120):
            print("-",end="")

        















    elif a==4:
        pass
    elif a==5:
        pass

profile()