import pandas as pd
import time
from tqdm import tqdm
import operator

df = pd.read_excel('review.xlsx')

assumed_number_of_restaurants = 1000

assigned_competitor_average_rating = 3.5

cool_score = 0

restaurants_ratings = dict()

review_scores = dict()
optimum_review_scores = dict()

ridlist = df['rid'].tolist() 
data_lines = len(ridlist)

def get_user_score(number_of_reviews, rating):
    score = number_of_reviews * rating
    return score

def analyze(n):
    for i in  tqdm(range(data_lines)):
        rid = df['rid'][i]
        # numberOfFriends = int(df['user_numberoffriends'][i])
        numberOfReviews = int(df['user_numberofreviews'][i])
        rating = int(df['rating'][i])
        # no_of_useful = int(df['numberofuseful'][i])
        # no_of_funny = int(df['numberoffunny'][i])
        # no_of_cool = int(df['numberofcool'][i])

        user_score = get_user_score(numberOfReviews, rating)
        optimum_user_score = get_user_score(numberOfReviews,5)
        if rid in review_scores:
            review_scores[rid] +=  user_score
            optimum_review_scores[rid] += optimum_user_score
        else:
            review_scores[rid] = user_score
            optimum_review_scores[rid] = optimum_user_score

    for rid in review_scores:
        rating = (review_scores[rid]/optimum_review_scores[rid])*5
        restaurants_ratings[rid] = float("{0:.2f}".format(rating))
    top_competitors = dict(sorted(restaurants_ratings.items(), key=operator.itemgetter(1), reverse=True)[:n])
    return restaurants_ratings,top_competitors
  