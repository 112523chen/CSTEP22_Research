import pandas as pd
import numpy as np
number_of_reviews = airbnb_search_details['number_of_reviews']
condlist = [number_of_reviews == 0, number_of_reviews.between(1,5),number_of_reviews.between(5,15),number_of_reviews.between(1,40),number_of_reviews>40]
choicelist = ['NO','FEW','SOME','MANY','A LOT']
airbnb_search_details['reviews_qualification'] = np.select(condlist,choicelist)
airbnb_search_details[['price','reviews_qualification']]