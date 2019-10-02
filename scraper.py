import requests
import re

def find_a_tag(tag, url = 'https://en.wikipedia.org/wiki/Asgardia'):
    
    content = requests.get(url)
    if content.status_code == 200:
        print("Server connection established.")
    else:
        print("Server has problem with connection. Problem nr is: " + content.status_code)
    
    text = content.text
    
    tags = ['body','head','html']
    if tag in tags:
    
        pattern = re.compile(rf'\n')
        text = re.sub(pattern,' ', text)
        pattern = re.compile(rf"<{tag}>.*</{tag}>|<{tag}.+</{tag}>|<{tag}.+>")
        
    else:
        pattern = re.compile(rf"<{tag}>.*</{tag}>|<{tag}.+</{tag}>|<{tag}.+>")
    
    matches = pattern.findall(text)

    if matches:
        print('There is a match')
        num = int(input('How many elements of list would you like to print. Max is: ' + str(len(matches)) + '\n'))
        for match in range(num):
            print (matches[match] + '\n')
    else:
        print('There was no match')

find_a_tag(tag = input("Please enter a tag you would like to search: "))