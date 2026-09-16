def exponential_moving_average(values: list, alpha: float) -> list:
    """
    Returns the exponential moving average at every position.
    """
    l = len(values)
    EMA = []
    EMA.append(values[0])
    for i in range(1,l):
        EMA_i = alpha*values[i] + (1-alpha)*EMA[i-1]
        EMA.append(EMA_i)
    return EMA
    