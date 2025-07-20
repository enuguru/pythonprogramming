from collections import defaultdict
import csv

def read_file(file_path):
    """
    Reads and parses a CSV file from the given file path. Returns the contents as 
    a list of rows, where each row is represented as a list of strings.

    Args:
    file_path (str): The path to the CSV file to be read.

    Returns:
    list: A list of rows from the CSV file, where each row is a list of strings.
    """
    with open(file_path, mode='r') as file:
        data = list(csv.reader(file))
    return data

def extract_movie_ratings(data):
    """
    Extracts movie ratings from the given dataset.

    Args:
        data (list of list): The rows of movie data, with a header as the first row.
                             Assumes the movie title is at index 0 and rating at index 2.

    Returns:
        dict: Keys are movie titles, values are lists of their ratings as floats.
    """
    movie_ratings = defaultdict(list)
    for row in data[1:]:
        try:
            title = row[0]
            rating = float(row[2])
            movie_ratings[title].append(rating)
        except (IndexError, ValueError):
            # Skip rows with missing or invalid data
            continue
    return dict(movie_ratings)

def get_average_ratings(movies_dict):
    """
    Calculate the average ratings for movies from a dictionary.

    This function processes a dictionary where each key is a movie title, and the
    corresponding value is a list of numerical ratings for that movie. It computes
    the average rating for each movie and returns these averages in a new
    dictionary.

    Parameters:
        movies_dict: dict
            A dictionary where keys are strings representing movie titles, and
            values are lists of numerical ratings (float or int) for each movie.

    Returns:
        dict
            A dictionary where each key is a movie title (string) and its value is
            the calculated average rating (float).
    """
    avg_ratings = {}
    for movie in movies_dict:
        ratings = movies_dict[movie]
        avg = sum(ratings) / len(ratings)
        avg_ratings[movie] = avg
    return avg_ratings

def print_movie_ratings(movie_ratings):
    """
    Prints the ratings of each movie provided in a dictionary.

    The function takes a dictionary containing movie titles as keys and
    their corresponding ratings as values, and it prints each movie 
    title along with its ratings in an organized manner.

    Args:
        movie_ratings (dict): A dictionary where keys are movie titles (str) and 
            values are their ratings (str, int, or float).

    Returns:
        None
    """
    print("Movie Ratings:")
    for movie, ratings in movie_ratings.items():
        print(f"{movie}: {ratings}")

def print_average_ratings(avg_ratings):
    """
    Print the average ratings of movies in a formatted output.

    This function takes a dictionary of movie titles and their average ratings
    and prints each movie with its corresponding rating in a formatted manner.
    The ratings are displayed with two decimal places.

    Parameters:
        avg_ratings (dict[str, float]): A dictionary where the keys are movie titles
            (strings) and the values are their average ratings (floats).

    Returns:
        None
    """
    print("\nAverage Ratings:")
    for movie, avg in avg_ratings.items():
        print(f"{movie}: {avg:.2f}")

def print_top_movies(avg_ratings):
    """
    Prints the top 5 movies with their average ratings in descending order.

    This function takes a dictionary of movie names and their corresponding average
    ratings and displays the top 5 movies along with their ratings. The results are
    sorted from the highest to the lowest average rating.

    Arguments:
        avg_ratings (dict): A dictionary where keys are movie names (str) and values
            are their average ratings (float).

    """
    print("\nTop Movies:")
    sorted_movies = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
    for movie, rating in sorted_movies[:5]:
        print(f"{movie}: {rating:.2f}")

def main():
    """
    Main function to execute the program workflow.

    Summary:
    This main function serves as the entry point to the program. It loads
    data from a CSV file containing movie information, processes the data
    to extract ratings for movies, calculates average ratings, and then
    displays the extracted data, average ratings, and top-rated movies.

    """
    file_path = 'movies.csv'
    data = read_file(file_path)
    movie_ratings = extract_movie_ratings(data)
    average_ratings = get_average_ratings(movie_ratings)
    
    print_movie_ratings(movie_ratings)
    print_average_ratings(average_ratings)
    print_top_movies(average_ratings)

main()