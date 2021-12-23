from bs4 import BeautifulSoup
import requests

def get_news(news_count: int): 

    html_doc = requests.get('https://habr.com/ru/news').text
    soup = BeautifulSoup(html_doc, 'html.parser')
    count = 0

    posts = []
    for item in soup.find_all('article'):
        count = count + 1

        posts.append({
            'caption' : item.find('h2').get_text(),
            'link': 'https://habr.com' + item.find('a', class_="tm-article-snippet__title-link")["href"]
        })

        if count >= news_count:
            break
        
    return posts