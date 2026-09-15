import numpy as np

def gini_impurity(y_left: list, y_right: list) -> float:
    """
    Returns the impurity as a float.
    """
    prop_left , prop_right ={} , {}
    for i in y_left:
        if( i in prop_left):
            prop_left[i]+=1
        else:
            prop_left[i] = 1
    for i in y_right:
        if( i in prop_right):
            prop_right[i]+=1
        else:
            prop_right[i]=1
    l_l,l_r = len(y_left) , len(y_right)
    L = l_l+l_r
    G_S_L , G_S_R = 1 , 1
    for i in prop_left:
        G_S_L = G_S_L - (prop_left[i]/l_l)**2
    for i in prop_right:
        G_S_R = G_S_R - (prop_right[i]/l_r)**2
    if(L != 0 ):    
        G_split = (l_l/L)*G_S_L + (l_r/L)*G_S_R
    else:
        G_split = 0
    return G_split