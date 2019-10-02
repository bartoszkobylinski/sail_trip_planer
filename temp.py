
import requests

import requests_cache
'''
requests_cache.install_cache('archiwum')

url  = 'https://en.wikipedia.org/wiki/Asgardia'

a = requests.get(url)

title_tag = '<title>'
title_num = a.text.find(title_tag)
title_num_end = a.text.find(title_tag[0] + '/' + title_tag[1:])

print(str(title_num) + ' beggining')
print(str(title_num_end) + ' end')

title = a.text[(title_num + len(title_tag)):title_num_end]
print(title)

#print(title)

#print(a.status_code)
#print(a.content)
#print(a.text)

def parser(url, tag):

    website = requests.get(url)
    if website.status_code:
        print('Server ok!')
    else:
        print('Server reached problem nr: ' + str(website.status_code))
    result = []

    return result

parser('http://www.google.com', 'h1')
'''
