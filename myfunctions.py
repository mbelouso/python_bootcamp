import numpy as np

# Use Numpy to write a function to create a large matrix of random numbers
def create_random_matrix(rows, cols, low=0, high=100):
    """
    Creates a matrix of random integers.

    Args:
        rows (int): Number of rows in the matrix.
        cols (int): Number of columns in the matrix.
        low (int): Lower bound for random integers (inclusive).
        high (int): Upper bound for random integers (exclusive).

    Returns:
        np.ndarray: A matrix of shape (rows, cols) filled with random integers.
    """
    return np.random.randint(low, high, size=(rows, cols))  