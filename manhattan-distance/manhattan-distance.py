import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x , y  = np.asarray(x,dtype = float) , np.asarray(y,dtype = float)
    return np.sum(abs(x-y) ,dtype = float)