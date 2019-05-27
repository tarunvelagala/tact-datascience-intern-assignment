from scraper import reviews_list
from sqlalchemy import Column, String, Integer, ForeignKey, TEXT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant_names'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    reviews = relationship('Reviews', backref='restaurant_name')


class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    review = Column(TEXT(convert_unicode=True))
    restaurant_id = Column(Integer, ForeignKey('restaurant_names.id'))


def get_session():
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session1 = Session()
    return session1


session = get_session()
for i in reviews_list:
    for key, value in i.items():
        restaurant = Restaurant(name=key)
        session.add(restaurant)
        session.commit()
        for j in value:
            review = Reviews(review=j, restaurant_name=restaurant)
            session.add(review)
session.commit()
session.close()
