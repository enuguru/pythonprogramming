import csv
from collections import defaultdict


def load_movie_ratings(filename):
    movie_ratings = defaultdict(list)
    movie_titles = {}

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            title = row['Title']
            rating = float(row['Rating'])
            movie_ratings[title].append(rating)
            movie_titles[title] = title
    return movie_titles, movie_ratings


def calculate_average_ratings(movie_ratings):
    avg_ratings = {}
    for movie_id, ratings in movie_ratings.items():
        avg_ratings[movie_id] = sum(ratings) / len(ratings)
    return avg_ratings


def filter_movies(avg_ratings, threshold):
    return {movie_id: avg for movie_id, avg in avg_ratings.items() if avg >= threshold}


def display_top_movies(movie_titles, avg_ratings, top_n=5):
    sorted_movies = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)[:top_n]
    print(f"{'Movie':<30} | {'Average Rating'}")
    print('-' * 45)
    for movie_id, avg in sorted_movies:
        print(f"{movie_titles[movie_id]:<30} | {avg:.2f}")


if __name__ == "__main__":
    FILENAME = 'movies.csv'
    THRESHOLD = 9.0
    TOP_N = 5

    movie_titles, movie_ratings = load_movie_ratings(FILENAME)
    avg_ratings = calculate_average_ratings(movie_ratings)
    filtered_movies = filter_movies(avg_ratings, THRESHOLD)
    display_top_movies(movie_titles, filtered_movies, top_n=TOP_N)
