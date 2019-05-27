from sqlalchemy import Column, String, Integer, ForeignKey, Text
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
    review = Column(Text)
    restaurant_id = Column(Integer, ForeignKey('restaurant_names.id'))


def get_session():
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()
    return session
