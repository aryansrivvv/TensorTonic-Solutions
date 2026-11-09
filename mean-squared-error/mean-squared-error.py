import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    N = len(y_pred)
    y_pred = np.asarray(y_pred, dtype = 'float')
    y_true = np.asarray(y_true, dtype = 'float')
    x = np.sum((y_pred-y_true)**2 , dtype = 'float')
    return float(x/N)