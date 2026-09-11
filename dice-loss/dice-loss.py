import numpy as np

def dice_loss(p: list, y: list, eps: float = 1e-8) -> float:
    """
    Returns the loss as a float.
    """
    p = np.asarray(p,dtype = float)
    y = np.asarray(y,dtype = float)
    a = float(np.sum(p*y, dtype = float))*2
    return float(1 - ((a+eps)/(np.sum(p)+np.sum(y)+eps)))