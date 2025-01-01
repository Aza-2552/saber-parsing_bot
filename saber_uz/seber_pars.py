import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from pprint import pprint


def pars_saber(category):
    load_dotenv()
    list_products = []
    URL = os.getenv('URL')
    HOST = os.getenv('HOST')
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', class_='col-12 col-sm-6 col-lg-4')

    for block in blocks:
        link = block.find('a').get('href')
        image = block.find('img').get('src')
        title = block.find('h4').get_text(strip=True)
        name_product = block.find('ul', class_='product__single-text-categories').get_text(strip=True)
        cost = block.find('span').get_text(strip=True)


        list_products.append({
            'link': link,
            'image': image,
            'title': title,
            'name_product': name_product,
            'cost': cost
        })

    return list_products


pars_saber('category/96/')
