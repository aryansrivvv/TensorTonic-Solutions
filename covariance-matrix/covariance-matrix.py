import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.asarray(X,dtype = float)
    N = float(1/(X.shape[0]-1))
    mu = np.mean(X,axis = 0 , dtype = float)
    X_c = X - mu 
    X_c_T = X.transpose()
    mat_m = np.dot(X_c_T,X_c)
    mat_m = mat_m*N
    return mat_m
    