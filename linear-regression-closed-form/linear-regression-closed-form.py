import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    y = np.asarray(y,dtype=float)
    X = np.asarray(X,dtype = float)
    X_T = X.T
    X_T_X_inv = np.linalg.inv(X_T@X)
    return list(np.linalg.multi_dot([X_T_X_inv,X_T,y]))