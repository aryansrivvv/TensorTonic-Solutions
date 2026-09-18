import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.asarray(x,dtype = float)
    n = x.size
    x_hat = np.mean(x)
    x_sample_std = np.sqrt(np.var(x, ddof=1))
    if x_sample_std != 0:
        return float((x_hat - mu0) / (x_sample_std / np.sqrt(n)))

    difference = x_hat - mu0
    if difference == 0:
        return 0.0
    return float(np.inf if difference > 0 else -np.inf)
    
                