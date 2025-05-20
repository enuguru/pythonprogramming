def geometric_progression_series(a, r, n):
    """
    Generates a geometric progression series.

    This function computes the terms of a geometric progression using the provided
    starting value, common ratio, and the number of terms. The geometric progression
    is a sequence of numbers where each term after the first is found by multiplying
    the previous one by a fixed, non-zero number called the common ratio.

    Parameters:
    a: int or float
        The first term of the geometric progression.
    r: int or float
        The common ratio by which each term is multiplied to get the next term.
    n: int
        The number of terms to be generated in the geometric progression.

    Returns:
    list
        A list containing the terms of the geometric progression, starting with the
        initial term and including `n` terms in total.
    """
    series = []
    for i in range(n):
        series.append(a * (r ** i))
    return series


# Example usage
first_term = 2
ratio = 3
num_terms = 5
result = geometric_progression_series(first_term, ratio, num_terms)
print(f"Geometric progression with a={first_term}, r={ratio}, n={num_terms}:")
print(result)
