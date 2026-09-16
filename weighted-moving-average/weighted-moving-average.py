def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    WMA = []
    sum_weights = sum(weights)
    l = len(values)
    w = len(weights)
    for i in range(l-w+1):
        w_s = 0
        for j in range(w):
            w_s += values[i+j]*weights[j]
        WMA.append(w_s/sum_weights)
    return WMA
        