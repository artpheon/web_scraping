from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_list_of_data(goods):
    names = []
    links = []
    prices = []
    for item in goods:
        names.append(item.a.string)
        links.append('https://www.webscraper.io' + item.a['href'])
        prices.append(item.h4.string)
    return list(zip(names, links, prices))

goods = []

for pg in range(1, 5):
    webpage = requests.get('http://webscraperio.us-east-1.elasticbeanstalk.com/test-sites/e-commerce/static/computers/tablets?page=' + str(pg))
    content = BeautifulSoup(webpage.content, 'html.parser')
    items = content.find_all('div', {'class': 'col-sm-4 col-lg-4 col-md-4'})
    for i in items:
        goods.append(i)

data = get_list_of_data(goods)
df = pd.DataFrame(data, columns = ['Name', 'Link', 'Price'])

try:
    df.to_excel('/home/hrobbin/python/web_scraping/new_pages.xlsx')
except:
    print('Error saving the dataframe!')
else:
    print('Written successfully')
finally:
    print('Exiting...')