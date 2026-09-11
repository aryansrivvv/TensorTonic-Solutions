import numpy as np

def vector_norm_3d(v: list) -> float | np.ndarray:
    """
    Returns a float or a NumPy array.
    """
    # v = np.asarray(v,dtype = float)
    # x = np.sum(v**2,axis = -1)
    # y = np.sqrt(x,dtype = float)
    # return y 
    values = np.asarray(v, dtype=float)
    norms = np.sqrt(np.sum(values ** 2, axis=-1))
    return float(norms) if norms.ndim == 0 else norms
