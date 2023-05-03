# Movie Recommendation Engine Using Collaborative Filtering Algorithm

import numpy as np


def collaborative_filtering(ratings_df):
    print('Ratings Dataframe Shape (rows, columns): ', ratings_df.shape, '\n')  # (number of rows, number of columns)

    # Create a user-item matrix
    ratings_matrix = ratings_df.pivot_table(index='user_id', columns='item_id', values='rating')

    # Replace missing values with 0
    ratings_matrix.fillna(0, inplace=True)

    # Normalize the result to a range of 0-1
    result_norm = ratings_matrix / ratings_matrix.max().max()

    # Scale the result to a range of 0-4
    result_scaled = (result_norm * 4).round(1)

    # Print the result
    print('Scaled Matrix Results:')
    print(result_scaled.to_string(), '\n')

    movie_names = ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']

    # Get indices of top recommended movies for each user
    top_movies_indices = np.argsort(-result_scaled, axis=1)

    # Look up movie names based on indices
    top_movies_names = [[movie_names[i] for i in row] for row in top_movies_indices]

    # Print top recommended movies for each user
    print('Top Recommended Movies:')

    for i, movie_list in enumerate(top_movies_names):
        movies_seen = list(ratings_df[ratings_df['user_id'] == i+1]['item_id'])
        recommended_movies = [movie for movie in movie_list if movie_names.index(movie)+1 not in movies_seen]

        print(f"User {i+1} - {', '.join(recommended_movies)}")
