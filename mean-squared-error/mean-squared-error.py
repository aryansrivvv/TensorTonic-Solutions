import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    """
    Returns the error as a float.
    """
    y_true = np.asarray(y_true,dtype = float)
    y_pred = np.asarray(y_pred,dtype = float)
    ssq = np.sum((y_pred-y_true)**2,dtype = float)
    inv_size = 1/float(np.size(y_true))
    return ssq*inv_size