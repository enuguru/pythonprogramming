import csv
from collections import defaultdict

def load_movie_ratings(filename):
    movie_ratings = defaultdict(list)
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['Title']
            try:
                rating = float(row['Rating'])
            except ValueError:
                continue
            movie_ratings[title].append(rating)
    return movie_ratings

def calculate_average_ratings(movie_ratings):
    avg_ratings = {}
    for title, ratings in movie_ratings.items():
        avg_ratings[title] = sum(ratings) / len(ratings)
    return avg_ratings

def filter_top_movies(avg_ratings, threshold=9.0):
    return {title: rating for title, rating in avg_ratings.items() if rating >= threshold}

def display_movies(movies):
    print("Top Rated Movies:")
    for title, rating in sorted(movies.items(), key=lambda x: x[1], reverse=True):
        print(f"{title}: {rating:.2f}")

if __name__ == "__main__":
    filename = "movies.csv"
    movie_ratings = load_movie_ratings(filename)
    avg_ratings = calculate_average_ratings(movie_ratings)
    top_movies = filter_top_movies(avg_ratings, threshold=9.0)
    display_movies(top_movies)