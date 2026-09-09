from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x.sort()
    l = len(x)
    num_x = np.asarray(x)
    total_sum = float(np.sum(num_x))
    mean = float(total_sum/l)
    median = float(np.median(num_x))
    vals, counts = np.unique(num_x, return_counts=True)
    mode = float(vals[np.argmax(counts)])
    return {
        "mean": mean , 
        "median":median, 
        "mode": mode
    }
    