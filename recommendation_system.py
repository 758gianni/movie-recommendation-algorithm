import sys
import pandas as pd
from content_filtering import content_filtering
from collaborative_filtering import collaborative_filtering

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python recommendation_system.py <algorithm-type>')
        sys.exit()

    algorithm_type = sys.argv[1]
    algorithm_type = algorithm_type.lower()

    if algorithm_type == 'content' or algorithm_type == 'con':
        user_df = pd.read_csv('./data/user_data.csv', header=None, skiprows=1)
        movie_df = pd.read_csv('./data/movie_data.csv', header=None, skiprows=1)
        content_filtering(user_df, movie_df)

    elif algorithm_type == 'collaborative' or algorithm_type == 'col':
        ratings_df = pd.read_csv('./data/ratings_data.csv')
        collaborative_filtering(ratings_df)

    else:
        print(f"Invalid algorithm '{algorithm_type}'. Valid options are 'content' / 'con' or 'collaborative' / 'col'.")
