import math

def rolling_std(values: list, window_size: int) -> list:
    """
    Returns the population standard deviation of every complete window.
    """
    result = []
    v = len(values)
    w = window_size
    # rolling std for first window 
    s , s_s =0 , 0
    for i in range(w):
        s += values[i]
        s_s += (values[i])**2
    mu_0 = s/w
    var_0 = s_s/w - mu_0**2
    result.append(var_0**0.5)
    for i in range(1,v-w+1):
        s = s-values[i-1]+values[i+w-1]
        s_s = s_s - values[i-1]**2 + values[i+w-1]**2
        mu_i = s/w
        var_i = s_s/w - mu_i**2
        result.append(var_i**0.5)
    return result
        
        