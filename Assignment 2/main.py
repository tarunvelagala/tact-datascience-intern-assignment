from scraper import reviews_list
from db import Restaurant, get_session, Reviews

session = get_session()
for i in reviews_list:
    for key, value in i.items():
        restaurant = Restaurant(name=key)
        session.add(restaurant)
        session.commit()
        for i in value:
            review = Reviews(review=i, restaurant_name=restaurant)
            session.add(review)
session.commit()
session.close()
