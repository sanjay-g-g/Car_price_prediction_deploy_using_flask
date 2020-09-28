# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 16:10:19 2020

@author: san_jay
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
#import flasgger
from flasgger import Swagger


app=Flask(__name__)
Swagger(app)
pickle_in=open('random_forest_regression_model.pkl','rb')
rf_random=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return 'WELCOME ALL'


@app.route('/predict',methods=["Get"])
def car_prediction_rand():
    """ Let predict the car price.
    ---
    parameters:
        - name: Present_Price
          in: query
          type: number
          required: true
        - name: Kms_Driven
          in: query
          type: number
          required: true
        - name: Owner
          in: query
          type: number
          required: true 
        - name: num_year
          in: query
          type: number
          required: true
        - name: Fuel_Type_Diesel
          in: query
          type: number
          required: true  
        - name: Fuel_Type_Petrol
          in: query
          type: number
          required: true 
        - name: Seller_Type_Individual
          in: query
          type: number
          required: true  
        - name: Transmission_Manual
          in: query
          type: number
          required: true 
    responses:
          200:
              description: The output values
                
         """       
    Present_Price=request.args.get('Present_Price')
    Kms_Driven=request.args.get('Kms_Driven')
    Owner=request.args.get('Owner')
    num_year=request.args.get('num_year')	
    Fuel_Type_Diesel=request.args.get('Fuel_Type_Diesel')
    Fuel_Type_Petrol=request.args.get('Fuel_Type_Petrol')
    Seller_Type_Individual=request.args.get('Seller_Type_Individual')
    Transmission_Manual=request.args.get('Transmission_Manual')	
    prediction=rf_random.predict([[Present_Price,Kms_Driven,Owner,num_year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
    print(prediction)
    return " THE PREDICTED VALUES CAR price is"+str(prediction)





if __name__=='__main__':
    app.run()
