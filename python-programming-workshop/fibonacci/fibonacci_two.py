def generate_ap_series(start, difference, n=20):
    """
    Generates an arithmetic progression (AP) series based on the given start, 
    common difference, and the number of terms.

    The function computes an arithmetic progression starting from the 
    specified starting value (`start`) and incrementing by the given common 
    difference (`difference`). By default, the series contains 20 terms unless 
    another value for the total number of terms is explicitly specified.

    Args:
        start (float): The starting value of the arithmetic progression.
        difference (float): The common difference between consecutive terms.
        n (int, optional): The total number of terms to generate in the series. 
            Defaults to 20.

    Returns:
        list[float]: A list containing the generated terms of the arithmetic 
        progression.
    """
    ap_series = []
    for i in range(n):
        term = start + (i * difference)
        ap_series.append(term)
    return ap_series


def main():
    """
    Generates and displays an arithmetic progression (AP) series
    based on provided start value and common difference. The
    resulting series is printed to the console.

    """
    # Example values
    start_value = 2
    common_difference = 3

    # Generate AP series
    series = generate_ap_series(start_value, common_difference)

    # Display the series
    print("Arithmetic Progression Series:")
    print(series)


if __name__ == "__main__":
    main()