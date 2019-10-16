import time
import datetime
import logging
import sqlite3
import requests_cache

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from credentials import credentials 
from data_extracting import extract_data

requests_cache.install_cache('bouyweather_archive_cache', expire_after=3600000)

user = credentials.get('user')
password = credentials.get('password')
logging.basicConfig(filename = f'logger_scraper {datetime.datetime.now()}.txt',level=logging.INFO)

#setting a browser 
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
path = "/home/bart/PythonProjects/flight/chrome/chromedriver"
browser = webdriver.Chrome(path,options=options)
browser.get("https://www.buoyweather.com")
browser.fullscreen_window()



def make_database():
    database_connection = sqlite3.connect('weather.db')
    database_connection.execute("DROP TABLE IF EXISTS Days")
    database_connection.commit()

    try:
        with database_connection:
            database_connection.execute("""CREATE TABLE Dates(
                Id INTEGER PRIMARY KEY NOT NULL,
                Dates TEXT 
            )
            """)
    except sqlite3.OperationalError as error:
        logging.warning(error)
    try: 
        with database_connection:
            database_connection.execute("""CREATE TABLE Daysquaters(
                Id INTEGER PRIMARY KEY NOT NULL,
                SecondAM TEXT,
                EightAM TEXT,
                SecondPM TEXT,
                EightPM TEXT
            )
            """)
    except sqlite3.OperationalError as error:
        logging.warning(error)
    try:
        with database_connection:
            database_connection.execute("""CREATE TABLE Conditions(
                Id INTEGER PRIMARY KEY NOT NULL,
                Windspeed INTEGER,
                Gaust INTEGER,
                WDirection TEXT,
                Wave INTEGER,
                Wavepeak INTEGER,
                Wavedirection TEXT,
                Periods INTEGER
            )
            """)
    except sqlite3.OperationalError as error:
        logging.warning(error)


def login_user(user, password):
    #Function to go through login page on a website
    time.sleep(seconds)
    # Finding and clicking on a Sign in button on html
    browser.find_element_by_xpath('//*[@id="top"]/div/nav/ul/li[3]/a').click()
    # Finding and filling up an email to log in
    browser.find_element_by_id("email").send_keys(user)
    # Findirng and fillig up a password to log in
    browser.find_element_by_id("password").send_keys(password)
    # Finding and clicking on a Sign in button
    browser.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[2]/form/button').click()

latitude = "59.50"
longitude = "10.50"
seconds = 10
def navigate_to_point(latitude,longitude):
    # Function to go to given coordinates
    time.sleep(seconds)
    try:
        browser.find_element_by_xpath('//*[@id="main"]/div/section/div/a[1]').click()
    except Exception as error:
        logging.warning(error)
    time.sleep(seconds)
    browser.find_element_by_id('custom-loc-toggle').click()
    time.sleep(seconds)
    browser.find_element_by_id('custom-lat').send_keys(latitude)
    browser.find_element_by_id('custom-lon').send_keys(longitude)
    browser.find_element_by_id('custom-latlon').click()
    browser.find_element_by_xpath('//*[@id="map-container"]/div/div[2]/div[3]/div/a').click()

def get_data_point():
    data_list = []
    all_days = browser.find_elements_by_class_name('day')
    for day in all_days:
        day = day.text.replace('\n',' ')
        data_list.append(day)
    return data_list     


def main():
    pass   

#Chrome instalation function to do

login_user(user,password)
navigate_to_point(latitude,longitude)
#make_database()
#function to making database has to be added
a = extract_data(get_data_point())
#function to inserting to database
#function to shedulle job
#install flask






