import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import pickle
import pandas as pd
import category_encoders as ce
import numpy as np
import json
from geopy.geocoders import Nominatim
from utils.fraud_prediction import FraudPrediction


app = Flask(__name__)
CORS(app)

# logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # print("---------------received data-------------")
    # print(data)
    # df = pd.DataFrame([data])
    # df['merch_lat'] = df['merchantLocation']
    # df['hour'] = pd.to_datetime(df['timeOfTransaction'], format='%H:%M').dt.hour
    # df['amt_log'] = np.log(pd.to_numeric(df['amount']))
    # logging.info("before WOE encoding:\n%s", df.to_string())
    # df['category_WOE'] = df['category'].apply(lambda x: get_woe_value('category', x))
    # df['job_WOE'] = df['job'].apply(lambda x: get_woe_value('job', x))
    # df['city_WOE'] = df['city'].apply(lambda x: get_woe_value('city', x))
    # df['cc_num_frequency'] = 2556
    # location = self.locator.geocode(data['city'])
    #     if location:
    #         data['merch_lat'] = location.latitude
    #     else:
    #         # Default latitude if location not found
    #         data['merch_lat'] = 1
    # df.drop(['city','job','category','creditCardNumber','amount','timeOfTransaction','merchantLocation'],axis=1, inplace=True)
    # logging.info("Final DF:\n%s", df.to_string())

    fp = FraudPrediction()
    prediction = fp.predict(data)
    return jsonify({"prediction":f"{prediction}"})
    #prediction = False #placeholder for demonstration
    #prediction = model.predict(df_encoded)
    #return jsonify({"prediction":prediction})

if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.INFO)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)