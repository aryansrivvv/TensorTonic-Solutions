import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    v = np.asarray(v,dtype = float)
    x = np.sum(v**2,axis = -1)
    y = np.sqrt(x,dtype = float)
    return y 