import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    x = np.asarray(x,dtype = float)
    vec_erf = np.vectorize(math.erf)
    GELU_x = x * (1 + vec_erf(x / np.sqrt(2))) / 2
    return GELU_x