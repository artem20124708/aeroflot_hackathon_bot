from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

def roadDocsParse():
    url = 'https://www.aeroflot.ru/ru-ru/information/preparation/regulations_papers'
    payload={}
    headers = {'Cookie': 'session-cookie=1714a2768b2780dd8b33d0c318991a242115e6d86ee3196e4b9d0468ea070a06735615f64f0842b2eddabd0b2c492a4f', 'User-Agent':'PostmanRuntime/7.29.2'}
    response = requests.request("GET", url, headers=headers, data=payload)
    f = open('regulations_papers.html','w+')
    # работа с файлом

    f.write(response.text)

    f.close()
    i=0
    j=1
    te=''
    with open("regulations_papers.html", "r") as f:

        contents = f.read()

        soup = BeautifulSoup(contents, 'lxml')
                
        for child in soup.recursiveChildGenerator():
            if child.name=='h2' and j==1:
                j += 1
                te += child.text
                te += '\n'
            if child.name=='p':
                i += 1
                if i>=4 and i<=9:
                    te += child.text
    roadDocs_msg=(te) 
    return(roadDocs_msg)