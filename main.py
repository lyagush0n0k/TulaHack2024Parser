from bs4 import BeautifulSoup
import requests

# Download search results page
main_url = 'https://visittula.com/places/restorany/restorani/'
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"}

def get_soup(url):
    res = requests.get(url, headers=headers)
    return BeautifulSoup(res.text, 'html.parser')

restorani_pages = get_soup(main_url)
restaurants = restorani_pages.find_all('div', class_='places-list-itm')

for restaurant in restaurants:
    title = restaurant.find('div', class_='places-list-itm-body-more-info').find(text=True).strip()
    adres = restaurant.find('div', class_='places-list-itm-body-more-address').find(text=True).strip()
    print(title, adres)
