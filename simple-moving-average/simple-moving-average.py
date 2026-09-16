def simple_moving_average(values: list, window_size: int) -> list:
    """
    Returns the mean of every complete sliding window.
    """
    SMA = []
    n = len(values)
    # Lets calculate SMA[0]
    s_0 = 0
    for i in range(window_size):
        s_0 += values[i]
    SMA.append(s_0/window_size)

    for i in range(1,n-window_size+1):
        s_0 = s_0 - values[i-1] + values[i+window_size-1]
        SMA.append(s_0/window_size)
    return SMA