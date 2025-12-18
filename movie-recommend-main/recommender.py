import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ast import literal_eval

# 데이터 준비
movies = pd.read_csv('tmdb_5000_movies.csv')
movies = movies[['title', 'genres']]
movies['genres'] = movies['genres'].apply(literal_eval)
movies['genres'] = movies['genres'].apply(lambda x: ' '.join([d['name'] for d in x]))

# 벡터화 및 유사도 계산
count_vect = CountVectorizer(ngram_range=(1, 2))
genre_mat = count_vect.fit_transform(movies['genres'])
genre_sim = cosine_similarity(genre_mat, genre_mat)
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]

# 추천 함수
def get_recommendations(title, top_n=10):
    if title not in movies['title'].values:
        return []
    idx = movies[movies['title'] == title].index[0]
    sim_idxs = genre_sim_sorted_ind[idx][1:top_n+1]
    return movies.iloc[sim_idxs]['title'].tolist()