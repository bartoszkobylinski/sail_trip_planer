import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup




def get_url():
    url = input("What website would you like to parse? ")
    return url
def parse_website(url):
    try:
        content = requests.get(url)

        soup = BeautifulSoup(content.text, 'html.parser')
        links_list = []
        for a in soup.find_all('a', href=True):
                links_list.append(a['href'] + '\n')
                
        return links_list
    except Exception as e:
        log_exception(e)
        print('Something went wrong. Check a logger for further information.')

def get_correct_link(links_list):
    pattern = re.compile(rf"/wiki/.*")
    
    for match in re.findall(pattern,str(links_list)):
        print(match + '\n')
        

def find_paragraph(url):
    pass

def find_title(url):    
    pass
def get_link_from_parsed_website(links_file):
    with open(links_file,'r') as reader:
        pattern = re.compile(rf"/wiki/.+>")
        pattern1 = re.compile(rf"language")
        print(reader.read())


        #matches = pattern.findall(str(link_list))
        #for match in matches:
        #    print(match)
def log_exception(e):
    with open("logger.txt", 'a') as logger:
        logger.write(str(e) +  " at " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\n')

#get_correct_link(parse_website(get_url()))

#log_exception('bartek')

a = parse_website(get_url())
pattern = re.compile(rf"\A/wiki/")
pattern1 = re.compile(rf"\A/wiki/.+:")
pattern2 = re.compile(rf"\A/wiki/.+language")
for i in a:
    if pattern.search(i) :
        if not pattern1.search(i):
            if not pattern2.search(i):
                print('we got hit: ' + 'https://en.wikipedia.org'+ i)


'''
website = requests.get(url)
soup = BeautifulSoup(website.text, 'html.parser')
#print(soup)
for a in soup.find_all('a', href=True):
    with open('linki.txt','a') as f:
        f.write(a['href'])


for paragraph in par_list:
    print(paragraph.getText())
'''