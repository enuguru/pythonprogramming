# geometric_profession.py

def print_geometric_progression(a, r, n):
    """
    A geometric progression is a sequence where each term after the first is found by multiplying the previous term by a fixed, non-zero number called the common ratio.

    Parameters:
        a (int or float): The first term of the progression.
        r (int or float): The common ratio between terms.
        n (int): The number of terms to print.

    Returns:
        None

    Example:
        print_geometric_progression(2, 3, 5)
        # Output: 2 6 18 54 162 
    """
    term = a
    for i in range(n):
        print(term, end=' ')
        term *= r

if __name__ == "__main__":
    first_term = 2      # You can change the first term as needed
    common_ratio = 3    # You can change the common ratio as needed
    num_terms = 15

    print_geometric_progression(first_term, common_ratio, num_terms)