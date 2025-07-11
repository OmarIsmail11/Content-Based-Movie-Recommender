import pickle
import pandas as pd
import streamlit as st
import requests
import numpy as np


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c3c76c97b08eb613d4e98a165139e2e8".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def recommend(movie):
    movieIndex = movies[movies["title"] == movie].index[0]
    distances = similarity[movieIndex]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendedMovies = []
    recommendedMoviesPosters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendedMovies.append(movies.iloc[i[0]].title)
        recommendedMoviesPosters.append(fetch_poster(movie_id))
    return recommendedMovies, recommendedMoviesPosters


movies = pd.read_csv("movies.csv")
similarity = np.load('similarity.npz')['similarity']

movieTitles = movies["title"].values

st.title("Movie Recommender System")
selected_movie_name = st.selectbox("Search for a movie", movieTitles)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
