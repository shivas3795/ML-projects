# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:37:13 2021

@author: satya
"""

import uvicorn
from fastapi import FastAPI
from bank_note import banknote
import pickle

#create app object
app = FastAPI()
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

#index route, opens automatically on 127.0.0.1:8000
@app.get('/')
def index():
    return {'message':'Hello, world'}

#opens on 127.0.0.1:8000/'name'
@app.get('/welcome')
def get_name(name: str):
    return {'welcome to home':f'{name}'}

#api for loading classifier pickle model from banknote class
@app.post('/predict')
def predict_banknote(data:banknote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosy=data['curtosy']
    entropy=data['entropy']
        
    prediction=classifier.predict([[variance,skewness,curtosy,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
            'prediction': prediction
            }

#run using uvicorn
if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn main(file name):app (app name) --reload   
#run above line in cmd  
#'127.0.0.1:8000/docs' runs open api (extended swagger version)