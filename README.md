# Content-Based-Movie-Recommender
![image](https://github.com/user-attachments/assets/2206b24e-94cf-4e32-a12d-b558cedfdcf4)
# About
This project is a Content-Based Movie Recommender System that suggests movies based on their similarity to a selected title. It analyzes movie metadata such as genre, keywords, cast and director to compute similarity between films.

The recommendation engine uses natural language processing (NLP) techniques like vectorization and cosine similarity to measure how closely related two movies are. A  Streamlit frontend allows users to select a movie and instantly receive a list of similar titles,  with posters fetched from the TMDb API.

Model was built using Scikit-learn and NLTK. The application is deployed on Streamlit Cloud, making it easily accessible from any browser with no installation required.

## Features
### 📄 Metadata Fusion
Combines multiple text fields into a unified "tag" for more accurate vectorization and comparison.

### 🖼️ Dynamic Poster Fetching
Retrieves high-quality movie posters using the TMDb API to enhance user experience.

### ⚡ Precomputed Similarity Matrix
Utilizes .csv and .npz files to store and load precomputed data, ensuring fast and responsive performance.

### 🌐 Deployed on Streamlit Cloud
Fully accessible online so no setup required. Just open the app in your browser and start exploring.

### 🧪 Simple, Interactive UI
Built with Streamlit for a clean and intuitive user experience.

## Demo
https://github.com/user-attachments/assets/5e691811-bdf1-4261-ac59-d908c07b135f

## How to use               
You can access the project at the following link: https://goated-movie-recommender.streamlit.app/
