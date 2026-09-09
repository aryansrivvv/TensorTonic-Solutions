import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x_np = np.asarray(x , dtype = float)
    x_var = float(np.var(x_np))
    x_len = float(x_np.size)

    s_s = (x_len/(x_len-1))*x_var
    return {
        "variance": s_s , 
        "standard_deviation" : float(np.sqrt(s_s))
    }
    