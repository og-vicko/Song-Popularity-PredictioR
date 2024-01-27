import pandas as pd 
import streamlit as st 
import pickle 
import joblib

model = joblib.load('SongPopularityPrediction.joblib')

st.title('Song Popularity Predictor')

song_duration_ms = st.text_input('Song duration ms')
acousticness = st.text_input('Acousticness')
danceability = st.text_input('Danceability')
energy = st.text_input('Energy')
instrumentalness = st.text_input('Instrumentalness')
key = st.text_input('Key')
liveness = st.text_input('Liveness')
loudness = st.text_input('Loudness')
audio_mode = st.text_input('Audio Mode')
speechiness = st.text_input('Speechiness')
tempo = st.text_input('Tempo')
time_signature = st.text_input('Time Signature')
audio_valence = st.text_input('Audio Valence')

def predict(song_duration_ms, acousticness, danceability, energy, instrumentalness,
             key, liveness, loudness, audio_mode, speechiness, tempo, time_signature, audio_valence):
    try:
        #Convert inputs to float and create dataframe
        input_data= {
            'song_duration_ms': float(song_duration_ms),
            'acousticness': float(acousticness),
            'danceability': float(danceability),
            'energy': float(energy),
            'instrumentalness': float(instrumentalness),
            'key': float(key),
            'liveness': float(liveness),
            'loudness': float(loudness),
            'audio_mode': float(audio_mode),
            'speechiness': float(speechiness),
            'tempo': float(tempo),
            'time_signature': float(time_signature),
            'audio_valence': float(audio_valence),
        }

        X = pd.DataFrame([input_data])

        #Make prediction
        prediction = model['model'].predict(X)[0]

        #Display result
        popularity_classes = {0: "Unpopular", 1: "Popular"}
        popularity = popularity_classes.get(prediction, 'Unknown')
        st.success(f'This song is going to be {popularity}')

    except ValueError:
        st.error("Please enter valid numbers")


# Button to make prediction

if st.button('predict'):
    predict(song_duration_ms, acousticness, danceability, energy, instrumentalness,
             key, liveness, loudness, audio_mode, speechiness, tempo, time_signature, audio_valence)
