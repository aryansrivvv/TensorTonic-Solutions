import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    m = len(A)
    n = len(A[0])
    A_transpose = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            A_transpose[i].append(A[j][i])
    A_T = np.asarray(A_transpose)
    return A_T
