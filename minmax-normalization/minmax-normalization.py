import numpy as np

def minmax_scale(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns a floating-point NumPy array matching the shape of X.
    """
    X = np.asarray(X,dtype = float)
    x_min = np.min(X,axis = axis , keepdims=True)
    x_max = np.max(X,axis = axis , keepdims=True)
    range_x = x_max-x_min
    return np.where(range_x<eps , 0.0 , (X-x_min)/range_x)