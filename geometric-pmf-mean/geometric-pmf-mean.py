import numpy as np

def geometric_pmf_mean(k: list, p: float) -> dict:
    """
    Returns a dictionary with pmf and mean.
    """
    k = np.asarray(k,dtype = float)
    z = np.asarray(p*((1-p)**(k-1)),dtype = float)
    return {
        "pmf": z, 
        "mean": 1/p
    }