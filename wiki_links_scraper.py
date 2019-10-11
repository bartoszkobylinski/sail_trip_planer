import requests
import requests_cache
import re
import sqlite3

from datetime import datetime
from bs4 import BeautifulSoup

requests_cache.install_cache('weather_archive_cach', expire_after=36000)

#Database functions

database_conn = sqlite3.connect('url_and_data.db')
cursor = database_conn.cursor()
database_conn.execute("DROP TABLE IF EXISTS Urls")
database_conn.commit()

try:
    with database_conn:
        database_conn.execute("""CREATE TABLE Urls ( 
            Urls TEXT, 
            Title TEXT, 
            Paragraph TEXT)""")
except sqlite3.OperationalError as error:
    log_exception(error)
    print("Table couldn't be created!")
print('Table created!')

def insert_data(url, title, paragraph):
    database_conn = sqlite3.connect('url_and_data.db')
    with database_conn:
        try:
            cursor.execute("INSERT INTO Urls VALUES (:Urls, :Title, :Paragraph)",{'Urls':url,'Title':title,'Paragraph':paragraph})
            #print(url +' with title: '+ title +' and paragraph: ' + paragraph + ' has been added to a database!')
        except TypeError as error:
            log_exception(error)
    database_conn.close()

links_list_level_0 = []
links_list_level_1 = []
links = []
counter = 0



def log_exception(error):
    with open("logger.txt", 'a') as logger:
        logger.write(str(error) +  " at " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')
  

def get_url_from_user(counter):
    url = 'https://en.wikipedia.org/wiki/Asgardia'
    print("What website would you like to parse? Would you like to start with Asgardia? If not just press 1 and paste your own website.:" + '\n')
    if input() == str(1):
        url = input('Paste your website: ')
    links_list_level_0.append(url)
    return url
    
def parse_website(url):
    try:
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        return soup
    except Exception as error:
        log_exception(error)
        print('Something went wrong with parsing. Check a logger for further information.')


def find_paragraph(soup):
    try:
        paragraph = soup.find('p')
        return paragraph.text
    except TypeError as error:
        log_exception(error)
        print('TypeError has occured finding paragraph. Check log!')
    except AttributeError as error:
        log_exception(error)
        print('AttributeError has occured searching paragraph. Check log!')
    except Exception as error:
        log_exception(error)
def find_title(soup):    
    try:
        title = soup.find('title')
        return title.text
    except TypeError as error:
        log_exception(error)
        print('TypeErrer has occured finding title. Check log!')
    except AttributeError as error:
        log_exception(error)
        print('AttributeError has occured searching title. Check log!')
    except Exception as error:
        log_exception(error)

def make_file(url, paragraph, title):
    with open('links_with_t_and_p.txt','a') as data_file:
        try:
            data_file.write(url + ': with a title as: ' + title + " and par as p: " + paragraph + '\n')
        except TypeError as error:
            log_exception(error)
            print(f'TypeError has occured writing {error} to the file. Check log!')
        except Exception as error:
            log_exception(error)

def extract_links(soup):
    try:
        links_list = []
        for a in soup.find_all('a', href=True):
            pattern = re.compile(rf"\A/wiki/")
            pattern1 = re.compile(rf"\A/wiki/(.+:)|(.+#)")
            pattern2 = re.compile(rf"\A/wiki/.+language")
            if pattern.search(a['href']) :
                if not pattern1.search(a['href']):
                    if not pattern2.search(a['href']):
                        links_list.append('https://en.wikipedia.org'+ a['href'])
            links_list = list(set(links_list))
        return links_list
    except Exception as e:
        log_exception(e)
        print("Soup file's problem. Check a logger for further information.")


def main_program(counter):
    while counter < 3:
        if counter == 0:
            soup = parse_website(get_url_from_user(counter))
            paragraph = find_paragraph(soup)
            title = find_title(soup)
            url = links_list_level_0[0]
            make_file(url, paragraph,title)
            insert_data(url,title,paragraph)
            links = extract_links(soup)
            print(str(len(links)) + ' that is len level 0.')
            counter +=1
        elif counter == 1:
            for url in links:
                soup = parse_website(url)
                paragraph = find_paragraph(soup)
                title = find_title(soup)
                make_file(url, paragraph,title)
                insert_data(url,title,paragraph)
                links2 = extract_links(soup)
                for link in links2:
                    links_list_level_1.append(link)
            links2 = list(set(links_list_level_1))    
            print(str(len(links_list_level_1)) + ' that is len level 1.')
            print(str(len(links2)) + ' that is len level 1 after sorting.')
            counter +=1
        else:
            for url in links2:
                soup = parse_website(url)
                paragraph = find_paragraph(soup)
                title = find_title(soup)
                make_file(url, paragraph,title)
                insert_data(url,title,paragraph)
            counter +=1

            return links2

main_program(0)
print('Program has ended.')
