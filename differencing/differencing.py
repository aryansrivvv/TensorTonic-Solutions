def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    current_series = list(series)  
    for _ in range(order):
        current_series = [current_series[j] - current_series[j-1] for j in range(1, len(current_series))]
    return current_series

