import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    x_sorted = sorted(x)
    n = len(x_sorted)
    q_res = []
    
    for i in q:
        r = (i / 100.0) * (n - 1)
        l, u = int(np.floor(r)), int(np.ceil(r))
        w = r - l
        P_q = (1 - w) * x_sorted[l] + w * x_sorted[u]
        q_res.append(P_q)
    return np.asarray(q_res)
