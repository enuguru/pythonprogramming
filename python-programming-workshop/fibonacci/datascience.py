import csv


def load_movie_ratings(file_path):
    """
    Reads a CSV file containing movie ratings and returns a dictionary where the keys
    are movie titles and the values are lists of ratings. Each row in the CSV file
    represents a movie and its associated rating. The ratings are parsed as floating-point
    numbers, and multiple ratings for the same movie are aggregated into a list.

    Args:
        file_path: Path to the CSV file containing movie ratings. The file must have
            a header row, with the movie title as the first column and the rating as
            the third column.

    Returns:
        Dictionary where the keys are movie titles (str) and the values are lists
        of ratings (list[float]).
    """
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        movie_ratings = {}
        for row in reader:
            title = row[0]
            rating = float(row[2])
            if title in movie_ratings:
                movie_ratings[title].append(rating)
            else:
                movie_ratings[title] = [rating]
    return movie_ratings


def calculate_average_ratings(movie_ratings):
    """
    Calculate average ratings for movies based on the provided ratings.

    This function computes the average rating for each movie in the provided 
    dictionary, where the keys are movie names and the values are lists of
    ratings. It iterates through the dictionary, calculates the average for
    each movie, and returns the result as a new dictionary.

    Parameters:
    movie_ratings: dict
        A dictionary where keys are strings representing movie names and values
        are lists of integers or floats representing the ratings for each movie.

    Returns: 
    dict
        A dictionary where keys are movie names and values are floats representing
        the average rating for each movie.
    """
    avg_ratings = {}
    for movie, ratings in movie_ratings.items():
        avg_ratings[movie] = sum(ratings) / len(ratings)
    return avg_ratings


def filter_movies_by_threshold(avg_ratings, threshold):
    """
    Filters movies based on their average rating compared to a given threshold.

    This function iterates over a dictionary of movie titles and their respective
    average ratings, selecting only those movies whose ratings meet or exceed the
    specified threshold and returning them as a new dictionary.

    Parameters:
    avg_ratings : dict[str, float]
        A dictionary where keys are movie titles (as strings) and values are their
        average ratings (as floats).
    threshold : float
        The minimum average rating a movie must have to be included in the 
        resulting dictionary.

    Returns:
    dict[str, float]
        A dictionary containing movies and their average ratings that meet or
        exceed the threshold.

    Raises:
    None 
    """
    return {movie: avg for movie, avg in avg_ratings.items() if avg >= threshold}


def display_top_movies(avg_ratings, top_n=5):
    """
    Displays the top N movies based on their average ratings in descending order.

    This function takes a dictionary of movie names and their corresponding average 
    ratings, sorts them in descending order by the ratings, and prints the top N 
    movies along with their average ratings. By default, the number of top movies 
    to be displayed is 5.

    Parameters:
        avg_ratings (dict): A dictionary where the keys are movie names (str) and 
            the values are their corresponding average ratings (float).
        top_n (int): The number of top movies to display. Defaults to 5.

    Returns:
        None
    """
    sorted_movies = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
    print(f"\nTop {top_n} Movies:")
    for movie, avg in sorted_movies[:top_n]:
        print(f"{movie}: {avg:.2f}")


def main():
    """
    Main execution function for processing movie ratings and displaying results.
    
    This function coordinates the overall flow of the program by loading movie ratings from a CSV
    file, calculating their average ratings, filtering movies based on a specified threshold,
    and displaying the top-rated movies.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        ValueError: If the file contains invalid or improperly formatted data.
    """
    file_path = 'movies.csv'
    movie_ratings = load_movie_ratings(file_path)
    avg_ratings = calculate_average_ratings(movie_ratings)

    print("Average Ratings for All Movies:")
    for movie, avg in avg_ratings.items():
        print(f"{movie}: {avg:.2f}")

    threshold = 9.0
    filtered = filter_movies_by_threshold(avg_ratings, threshold)
    print(f"\nMovies with Average Rating >= {threshold}:")
    for movie, avg in filtered.items():
        print(f"{movie}: {avg:.2f}")

    display_top_movies(avg_ratings, top_n=5)


if __name__ == "__main__":
    main()
