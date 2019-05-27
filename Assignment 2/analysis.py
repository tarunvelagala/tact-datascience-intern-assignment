from collections import Counter
from statistics import mean
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from db import get_session, Restaurant, Reviews

session = get_session()
reviews_list = []
sentiment_list = []
restaurant_data = session.query(Restaurant).all()

for i in restaurant_data:
    review_data = session.query(Reviews).filter(
        i.id == Reviews.restaurant_id).all()
    reviews_list.append({i.name: sum([tokenize.sent_tokenize(j.review) for j in review_data], [])})


def sentiment_scores(sentence):
    sent_obj = SentimentIntensityAnalyzer()
    sentiment_scores_dict1 = sent_obj.polarity_scores(sentence)
    return sentiment_scores_dict1


for i in reviews_list:
    for keys, values in i.items():
        # sentiment_pos_mean = mean([sentiment_scores(value)['pos'] for value in values])
        # sentiment_neg_mean = mean([sentiment_scores(value)['neg'] for value in values])
        # sentiment_neu_mean = mean([sentiment_scores(value)['neu'] for value in values])
        sentiment_compound_mean = mean([sentiment_scores(value)['compound'] for value in values])
        sentiment_list.append(
            {keys: sentiment_compound_mean})

print(sentiment_list)
