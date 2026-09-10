import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    v = np.asarray(v,dtype = float)
    l = v.size
    mat = np.zeros((l,l), dtype = v.dtype)
    indices = np.arange(l)
    mat[indices,indices] = v
    return mat