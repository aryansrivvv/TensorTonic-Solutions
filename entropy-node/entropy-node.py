import numpy as np

def entropy_node(y: list[int]) -> float:
    """
    Returns the Shannon entropy as a Python float.
    """
    total = len(y)
    result = 0 
    dict_y = {}
    for i in y:
        if(i in dict_y):
            dict_y[i] +=1 
        else:
            dict_y[i] = 1
    for i in dict_y:
        result -= (dict_y[i]/total)*np.log2(dict_y[i]/total)
    return float(result)