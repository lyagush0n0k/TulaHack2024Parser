from bs4 import BeautifulSoup
import requests
import csv


main_url = 'https://visittula.com/places/restorany/restorani/?PAGEN_1='
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"}
FILENAME = "users.csv"

def get_soup(url):
    res = requests.get(url, headers=headers)
    return BeautifulSoup(res.text, 'html.parser')


objects = []
j = 0

for i in range (0, 1, 1):
    restorani_pages = get_soup(main_url+str(i))
    restaurants = restorani_pages.find_all('div', class_='places-list-itm')
    for restaurant in restaurants:
        title = restaurant.find('div', class_='places-list-itm-body-more-info').find(text=True).strip()
        adress = restaurant.find('div', class_='places-list-itm-body-more-address').find(text=True).strip()
        link = restaurant.findAll('div', class_='places-list-itm-body')
        productDivs = restaurant.findAll('div', attrs={'class': 'places-list-itm-body'})
        for div in productDivs:
            print (div.find('a')['href'])
            restourant_info = get_soup("https://visittula.com" + div.find('a')['href'])
            for para in restourant_info.find_all("p", attrs={'style': 'text-align: left;'}):
                info_text = info_text + para.get_text().replace('\n', '')
    objects.append([j, title, adress, info_text])
    j += 1

with open(FILENAME, "w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(objects)
