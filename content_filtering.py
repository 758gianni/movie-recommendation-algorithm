# Movie Recommendation Engine Using Content Filtering Algorithm

import numpy as np


def content_filtering(user_df, movie_df):
    print('User Dataframe Shape (rows, columns): ', user_df.shape)  # (number of rows, number of columns)
    print('Movie Dataframe Shape (rows, columns): ', movie_df.shape)  # (number of rows, number of columns)

    if set(user_df.columns) != set(movie_df.columns):
        raise ValueError('Column names in user_data.csv and movie_data.csv do not match!')

    # Perform matrix multiplication and store the result in a new dataframe
    ratings_matrix = user_df.dot(movie_df.transpose())

    # Replace missing values with 0
    ratings_matrix.fillna(0, inplace=True)

    print('\nMatrix Results:')
    print(ratings_matrix, '\n')

    # Normalize the result to a range of 0-1
    result_norm = ratings_matrix / ratings_matrix.max().max()

    # Scale the result to a range of 0-4
    result_scaled = (result_norm * 4).round(1)

    # Print the result
    print('Scaled Matrix Results:')
    print(result_scaled, '\n')

    # Convert result_scaled Pandas DataFrame to a NumPy array (2-dimensional)
    result_scaled = result_scaled.to_numpy()

    movie_names = ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']

    # Get indices of top recommended movies for each user
    top_movies_indices = np.argsort(-result_scaled, axis=1)[:, 0:2]  # Get top 2 movies for each user

    # Look up movie names based on indices
    top_movies_names = [[movie_names[i] for i in row] for row in top_movies_indices]

    # Print top recommended movies for each user
    print('Top Recommended Movies:')

    for i, movie_list in enumerate(top_movies_names):
        print(f"User {i+1} - {', '.join(movie_list)}")
