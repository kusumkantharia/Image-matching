# -*- coding: utf-8 -*-
"""
@author: Kusum
"""

from flask import Flask,request
import numpy as np
import pickle
import pandas as pd 

from PIL import Image

app=Flask(__name__)

pickle_in = open("outdoor.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def upload():
    image1 = request.files['image1']
    image2 = request.files['image2']
    
    prediction=classifier.predict([[fname1,fname2]])
    return "The predicted value is"+ str(prediction)

if __name__=='__main__':
    app.run()