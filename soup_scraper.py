import requests
import requests_cache
import re

from datetime import datetime
from bs4 import BeautifulSoup

requests_cache.install_cache('weather_archive_cach', expire_after=36000)

links_list_level_0 = []
links_list_level_1 = []
links_list_level_2 = []
links_total = []
counter = 0

def log_exception(e):
    with open("logger.txt", 'a') as logger:
        logger.write(str(e) +  " at " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')


def remove_duplicate(link_list):
    link_list = list(set(link_list))
    return link_list
    

def get_url_from_user(counter):
    url = 'https://en.wikipedia.org/wiki/Asgardia'
    print("What website would you like to parse? Would you like to start with Asgardia? If not just press 1 and paste your own website.:" + '\n')
    if input() == str(1):
        url = input('Paste your website: ')
    links_list_level_0.append(url)
    counter +=1
    return url
    
def parse_website(url):
    try:
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'html.parser')
        return soup
    except Exception as e:
        log_exception(e)
        print('Something went wrong with parsing. Check a logger for further information.')

def find_paragraph(soup):
    paragraph = soup.find('p')
    return paragraph.text

def find_title(soup):    
    title = soup.find('title')
    return title.text

def make_file(url, paragraph, title):
    with open('file_with_data1.txt','a') as data_file:
        data_file.write(url + ': with a title as: ' + title + " and par as p: " + paragraph + '\n')

'''
def extract_links(soup):
    try:
        links_list = []
        for a in soup.find_all('a', href=True):
                links_list.append(a['href'])
        return links_list
    except Exception as e:
        log_exception(e)
        print("Soup file's problem. Check a logger for further information.")
'''
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
        return links_list
    except Exception as e:
        log_exception(e)
        print("Soup file's problem. Check a logger for further information.")

def get_correct_link(link_list):
    a = link_list
    pattern = re.compile(rf"\A/wiki/")
    pattern1 = re.compile(rf"\A/wiki/(.+:)|(.+#)")
    pattern2 = re.compile(rf"\A/wiki/.+language")
    b = []
    for i in a:
        if pattern.search(i) :
            if not pattern1.search(i):
                if not pattern2.search(i):
                    b.append('https://en.wikipedia.org'+ i)
    return b

def main_program(counter):
    while counter < 3:
        if len(links_list_level_0) == 0:
            soup = parse_website(get_url_from_user(counter))
            paragraph = find_paragraph(soup)
            title = find_title(soup)
            url = links_list_level_0[0]
            make_file(url, paragraph,title)
            links = extract_links(soup)
            correct_links = get_correct_link(links)
            correct_links = remove_duplicate(correct_links)
            print(str(len(links_list_level_0))+' that is len of level 0.')
            counter +=1
        elif len(links_list_level_0) !=0 and len(links_list_level_1) == 0:
            for url in correct_links:
                soup = parse_website(url)
                paragraph = find_paragraph(soup)
                title = find_title(soup)
                make_file(url,paragraph,title)
                links = extract_links(soup)
                correct_links_level1 = get_correct_link(links)
                correct_links_level1 = remove_duplicate(correct_links_level1)
                for link in correct_links_level1:
                    links_list_level_1.append(link)
                with open('links1_after.txt', 'w') as links_file:
                    for link in correct_links:
                        links_file.write(link + '\n')
            print(str(len(links_list_level_1)) + ' that is len level 1')
            counter +=1
        else:
            for url in correct_links_level1:
                soup = parse_website(url)
                paragraph = find_paragraph(soup)
                title = find_title(soup)
                make_file(url,paragraph,title)
                links = extract_links(soup)
                correct_links_level2 = get_correct_link(links)
                correct_links_level2 = remove_duplicate(correct_links_level2)
                for link in correct_links_level2:
                    links_list_level_2.append(link)
            counter +=1
            with open('links2_after.txt', 'w') as links_file:
                for link in links_list_level_2:
                    links_file.write(link + '\n')
            print(str(len(links_list_level_2)) + ' that is len level 2')




#main_program(0)
a = extract_links(parse_website(get_url_from_user(0)))
print(len(a))
a = list(set(a))
print(len(a))
