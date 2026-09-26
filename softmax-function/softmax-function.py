import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    x = np.asarray(x,dtype = float)
    x_max_row = np.max(x, axis = -1 , keepdims = True)
    y = np.exp(x - x_max_row)
    y_row_sum = np.sum(y, axis = -1 , keepdims = True)
    return y/y_row_sum
    