import requests
from bs4 import BeautifulSoup

reviews_list = []
base_url = 'https://www.yelp.com'
url = 'https://www.yelp.com/search?find_desc=Restaurants&find_near=cn-tower-toronto'
'''proxies1 = {'http': '193.200.151.69:40336',
            'https': '80.73.90.18:3128'
            }'''
page = requests.get(url)
soup_obj = BeautifulSoup(page.content, 'html.parser')

restaurant_list_links = soup_obj.findAll("h3", {
    'class': "lemon--h3__373c0__sQmiG heading--h3__373c0__1n4Of alternate__373c0__1uacp"})[6:13]

links_dict = {i.a.string: base_url + i.a['href'] for i in restaurant_list_links if i is not None}

for key, value in links_dict.items():
    review_page = requests.get(value)
    soup_obj = BeautifulSoup(review_page.content, 'html.parser')
    review_links_obj = soup_obj.findAll(
        'div', {'class': 'review-content'})
    reviews_list.append({key: [i.p.text for i in review_links_obj]})
