import joblib
import numpy as np
import  pandas as pd
from datetime import datetime as dt
import category_encoders as ce
import warnings 
import json
import random
from geopy.geocoders import Nominatim
warnings.filterwarnings('ignore') 



def get_woe_value(column_name, value):
    woe_dicts = {}
    with open(f'./dicts_woe/{column_name}.json', 'r') as f:
        woe_dicts[column_name] = json.load(f)
    
    if value in woe_dicts[column_name]:
        return woe_dicts[column_name][value]
    else:
        print(f"No WOE value found for '{value}' in {column_name} dictionary.")
        return None

class FraudPrediction:
    def __init__(self):
        self.model = joblib.load('./models/knn_ru.pkl')
        self.locator = Nominatim(user_agent="Geopy Library")
        
    def preprocess(self, data):

        # data['category'] = pd.Series(data['category'])
        # data['job'] = pd.Series(data['job'])
        # data['city'] = pd.Series(data['city'])
    
        data['age'] = int(data['age'])
        data['amount'] = float(data['amount'])
        data['hour'] = dt.strptime(data['timeOfTransaction'], '%H:%M').hour
        data['amt_log'] = np.log(data['amount'])
        # data['category_WOE'] = data['category'].apply(lambda x: get_woe_value('category', x))
        # data['job_WOE'] = data['job'].apply(lambda x: get_woe_value('job', x))
        # data['city_WOE'] = data['city'].apply(lambda x: get_woe_value('city', x))
        data['category_WOE'] = get_woe_value('category', data['category'])
        data['job_WOE'] =  get_woe_value('job', data['job'])
        data['city_WOE'] = get_woe_value('city', data['city'])
        data['cc_num_frequency'] = random.randint(0,1000)
        data['merchant_location'] = data['merchantLocation']
        # location = self.locator.geocode(data['city_WOE'])
        # if location:
        #     data['merch_lat'] = location.latitude
        # else:
        #     data['merch_lat'] = 1
        #data['merch_lat'] = 44.748

        # woe = ce.WOEEncoder()
        # data['category_WOE'] = 1
        # data['city_WOE'] = 1
        # data['job_WOE'] = 1
        # data['category_WOE'] = woe.fit_transform(data['category'], 1)
        # data['city_WOE'] = woe.fit_transform(data['city'], 1)
        # data['job_WOE'] = woe.fit_transform(data['job'], 1)
        # data['job_WOE'] =  31
        #data['merch_lat'] = 40.7128    # NYC lat
        
        # print("DataFrame before conversion:")
        # print(data)

        # columns = ['merch_lat', 'age', 'hour', 'amt_log', 'category_WOE', 'city_WOE', 'job_WOE', 'cc_num_frequency']
        # model_data = np.array([[data[column] for column in columns]], dtype=float)
            
        model_data = np.array([
            data['merch_lat'],
            data['age'],
            data['hour'],
            data['amt_log'],
            data['category_WOE'],
            data['city_WOE'],
            data['job_WOE'],
            data['cc_num_frequency']
        ], dtype=float).reshape(1, -1)

        print("DataFrame before conversion:")
        print(data)

        return model_data


    def predict(self, data):
        preproccess_data = self.preprocess(data)
        prediction = self.model.predict(preproccess_data)
        return prediction[0]