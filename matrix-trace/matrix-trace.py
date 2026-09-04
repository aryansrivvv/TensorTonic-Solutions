import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    n = len(A)
    tr = 0
    for i in range(n):
        tr += A[i][i]

    return tr