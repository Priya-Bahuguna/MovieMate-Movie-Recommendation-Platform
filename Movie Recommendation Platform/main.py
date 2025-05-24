import pandas as pd
import numpy as np
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

def convert(text):
    return [i['name'] for i in ast.literal_eval(text)]

def convert3(text):
    return [i['name'] for i in ast.literal_eval(text)[:3]]

def fetch_director(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return i['name']
    return ""

def collapse_list(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)
movies['cast'] = movies['cast'].apply(collapse_list)
movies['genres'] = movies['genres'].apply(collapse_list)
movies['keywords'] = movies['keywords'].apply(collapse_list)
movies['crew'] = movies['crew'].apply(lambda x: x.replace(" ", ""))
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'].apply(lambda x: [x])
new = movies[['movie_id', 'title', 'tags']]
new['tags'] = new['tags'].apply(lambda x: " ".join(x))

cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()

similarity = cosine_similarity(vector)

# Save files
pickle.dump(new, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Pickle files saved!")

