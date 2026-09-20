def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    res = []
    for i in range(1,len(series)):
        if (series[i-1]!= 0):
            p_i = (series[i]-series[i-1])/series[i-1]
            res.append(p_i)
        else:
            res.append(0.0)
    return res