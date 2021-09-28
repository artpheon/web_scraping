from bs4 import BeautifulSoup
import requests

def get_solutions() -> None:
    webpage = requests.get('https://webscraper.io/pricing')
    content = BeautifulSoup(webpage.content, 'html.parser')
    head = content.head
    body = content.body
    h2 = content.h2
    btn = body.button
    spans = btn.findChildren()
    result = content.find_all('div', {'class': 'box'})

    solutions = []
    for row in result:
        i = row.find('h2').text
        solutions.append(i)
    return solutions

