import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    x = np.asarray(X,dtype = float)
    mean_x = np.mean(x,axis = axis , keepdims = True)
    std_x = np.std(x,axis = axis , keepdims = True)
    return np.where( std_x > eps , (x-mean_x)/std_x , 0.0) 