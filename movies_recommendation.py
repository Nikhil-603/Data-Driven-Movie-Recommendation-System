# -*- coding: utf-8 -*-
"""movies recommendation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hEpClshftdXYQo_JFTw7PXGaiZKQWW2n
"""

import pandas as pd

movies=pd.read_csv('mdataset.csv')

movies.head(10)

movies.describe()

movies.info()

movies.isnull().sum()

"""# ***Feather Selection Part***






"""

movies.columns

movies=movies[['id','title','overview','genre']]

movies

movies['tags']=movies['overview']+movies['genre']

movies

new_movies = movies.drop(columns=['overview','genre'])

new_movies

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer(max_features=10000, stop_words='english')

cv

vector=cv.fit_transform(new_movies['tags'].values.astype('U')).toarray()

vector.shape

from sklearn.metrics.pairwise import cosine_similarity

sim=cosine_similarity(vector)

sim

new_movies[new_movies['title']=="The Godfather"].index[0]

def recommand(movies):
  index=new_movies[new_movies['title']==movies].index[0]
  distance = sorted(list(enumerate(sim[index])), reverse=True, key=lambda vector:vector[1])
  for i in distance[0:5]:
    print(new_movies.iloc[i[0]].title)

recommand("Iron Man")

import pickle

pickle.dump(new_movies, open('movies_list.pkl','wb'))

pickle.dump(sim, open('similarty.pkl','wb'))

pickle.load(open('movies_list.pkl', 'rb'))