import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load your movie dataset
movies = pd.read_csv('movies.csv')

# Combine text features: overview + genres (can extend to cast, director, etc.)
movies['tags'] = movies['overview'].fillna('') + " " + movies['genres'].fillna('')

# Convert text to vectors using Bag-of-Words model
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity matrix
similarity = cosine_similarity(vectors)

# Save similarity matrix to file
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# Save updated movies file with 'tags' column
movies.to_csv('movies.csv', index=False)
