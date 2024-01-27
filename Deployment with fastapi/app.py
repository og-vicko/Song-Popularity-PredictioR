from fastapi import FastAPI, File , Form, UploadFile
from pydantic import BaseModel
import pickle
import uvicorn
import numpy as np 
import pandas as pd 
import requests
from io import StringIO


app = FastAPI()


#CREATING THE CLASS FOR REQUUEST
class PopularityPredictor(BaseModel):
    song_duration_ms : float
    acousticness : float
    danceability : float
    energy : float
    instrumentalness : float
    key : float
    liveness : float
    loudness : float
    audio_mode : float
    speechiness : float
    tempo : float
    time_signature : float
    audio_valence : float


@app.get('/')
async def root():
    return {'message': 'Hi there! welcome'}

# predict_species
@app.post('/predict')
async def PopularityPredictorfunc(predictor: PopularityPredictor):

    #Generate a dictionary representation of the pydantic BaseModel
    data = predictor.model_dump()

    #Prepare the data in the format expected by the Mlflow model server
    data_input = [data]

    print(data_input)

    #define the MLFlow model server endpoint
    endpoint = "http://localhost:5000/invocations"

    #prepare the inference request payload
    inference_request = {'dataframe_records': data_input}
    print(inference_request)


    #Make the POST request to the MLflow model server and get the response
    response = requests.post(endpoint, json=inference_request)

    #Map the pprediction result to the corresponding species name
    popularity_mapping = {0: "Unpopular", 1: "Popular"}

    # Extract predition from response
    popularity_prediction = response.json().get('predictions')[0] #<--- Aliter: response.text[0]
    popularity = popularity_mapping.get(popularity_prediction, "unknown")

    # Return the species name as the prediction
    return {"prediction": popularity}

@app.post('/files')
async def batch_predict(file: bytes = File(...)):
    s = str(file, encoding = 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)

    inference_request = {"dataframe_records": df.to_dict(orient='records')}
    endpoint = "http://localhost:5000/invocations"
    response = requests.post(endpoint, json = inference_request)
    print(response)

    popularity_mapping = {0: "Unpopular", 1: "Popular"}
    predictions = response.json().get('predictions', []) 
    popularity = [popularity_mapping.get(pred, "unknown") for pred in predictions]

    return {"predictions": popularity}

