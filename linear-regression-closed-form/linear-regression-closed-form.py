import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    X = np.asarray(X,dtype = 'float')
    X_T = np.transpose(X)
    X_inv = np.linalg.inv(np.dot(X_T,X))
    return X_inv @ X_T @ y 
    