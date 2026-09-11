import numpy as np

def r2_score(y_true: list, y_pred: list) -> float:
    """
    Returns the coefficient of determination as a Python float.
    """
    x = np.asarray(y_true,dtype = float)
    y = np.asarray(y_pred,dtype = float)
    nm = float(np.mean(x))
    s_s_n = float(sum(np.asarray((x-nm)*(x-nm),dtype = float)))
    z = float(sum(np.asarray((x-y)*(x-y),dtype = float)))
    if(s_s_n != 0 ):
        return (1 - z/s_s_n)
    else:
        if (z==0):
            return 1.0
        else:
            return 0.0
    