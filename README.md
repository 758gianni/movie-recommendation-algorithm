
# Movie Recommendation Algorithm

Content filtering and collaborative filtering are two popular approaches to recommendation systems in machine learning.

Content filtering works by analyzing the features of items (such as movies) and recommending similar items based on those features. For example, if a user watches action movies, a content-based system might recommend other action movies with similar actors, directors, or genres.

Collaborative filtering, on the other hand, works by analyzing the behavior and preferences of multiple users and recommending items that other similar users have also liked. This approach is based on the assumption that users who have similar preferences in the past are likely to have similar preferences in the future. For example, if two users both enjoy action movies, a collaborative filtering system might recommend action movies that one user has liked and the other has not yet seen.

## Features

- Content-Based Filtering
- Collaborative-Based Filtering

## Run Locally

Clone the project

```bash
  git clone https://github.com/758gianni/movie-recommendation-algorithm
```

Go to the project directory

```bash
  cd movie-recommendation-algorithm
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the algorithm

```bash
  python recommendation_system.py <algorithm-type>
```

## FAQ

#### What input data is required for the code to work?

For content filtering, the code requires two CSV files: one containing user data and another containing movie data. For collaborative filtering, the code requires a CSV file containing user ratings data. These files should be located in a specific folder relative to the recommendation_system.py file, as indicated in the code.

#### How are the top recommended movies determined for each user?

For content filtering, the code performs matrix multiplication between the user dataframe and movie dataframe, normalizes and scales the result to a range of 0-4, and then gets the top 2 movies for each user based on the resulting matrix. For collaborative filtering, the code creates a user-item matrix, normalizes and scales the result, and then gets the top recommended movies for each user based on the resulting matrix.

## Acknowledgements

 - [26 Content based Recommender Systems](https://youtu.be/YMZmLx-AUvY)
 - [27 Collaborative Filtering](https://youtu.be/3oCtj29XeYY)
 - [Movie Recommender System using Python](https://youtu.be/R64Lh1Qwl_0)
 
## License

[MIT](https://choosealicense.com/licenses/mit/)
