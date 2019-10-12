import time
import datetime
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from credentials import credentials 

user = credentials.get('user')
password = credentials.get('password')


logging.basicConfig(filename = f'logger_scraper + {datetime.datetime.now()}.txt',level=logging.INFO)

#setting a browser 
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
path = "/home/bart/PythonProjects/flight/chrome/chromedriver"
browser = webdriver.Chrome(path,options=options)
browser.get("https://www.buoyweather.com")

def error_logger(error):
    with open(f'error logger + {datetime.datetime.now()} +.txt','w') as logger_file:
        logger_file.write(str(error))

def login_user(user, password):
    #Function to go through login page on a website
    time.sleep(30)
    # Finding and clicking on a Sign in button on html
    browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[3]/a').click()
    # Finding and filling up an email to log in
    browser.find_element_by_id("email").send_keys(user)
    # Findirng and fillig up a password to log in
    browser.find_element_by_id("password").send_keys(password)
    # Finding and clicking on a Sign in button
    browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/form/button').click()

latitude = "59.49"
longitude = "10.54"
seconds = 15
def navigate_to_point(latitude,longitude):
    # Function to go to given coordinates
    time.sleep(seconds)
    try:
        browser.find_element_by_xpath('//*[@id="main"]/div/section/div/a[1]').click()
    except Exception as error:
        error_logger(error)
    time.sleep(seconds)
    browser.find_element_by_id('custom-loc-toggle').click()
    time.sleep(seconds)
    browser.find_element_by_id('custom-lat').send_keys(latitude)
    browser.find_element_by_id('custom-lon').send_keys(longitude)
    browser.find_element_by_id('custom-latlon').click()
    browser.find_element_by_xpath('//*[@id="map-container"]/div/div[2]/div[3]/div/a').click()
def get_data_point():
    data_list = []
    div = browser.find_elements_by_class_name('wind-wave')
    for days in div:
        days = browser.find_elements_by_class_name('day')
        for timestep in days:
            timestep = browser.find_elements_by_class_name('timestep')
            for data in timestep:
                data = data.text.replace('\n',' ')
                data_list.append(data)
                logging.info(data)

def extract_data(data_list):
    pass

            
            
    
login_user(user,password)
navigate_to_point(latitude,longitude)
get_data_point()

