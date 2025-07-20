# Python program to create a simple arithmetic progression (AP) series

def arithmetic_progression(a, d, n):
    """
    Generate an arithmetic progression series.
    a: first term
    d: common difference
    n: number of terms
    """
    series = []
    for i in range(n):
        term = a + i * d
        series.append(term)
    return series

# Example usage
a = 2      # first term
d = 3      # common difference
n = 10     # number of terms

ap_series = arithmetic_progression(a, d, n)
print(ap_series)