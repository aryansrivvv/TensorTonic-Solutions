import numpy as np

def auc(fpr: list, tpr: list) -> float:
    """
    Returns the area as a float.
    """
    AUC = 0 
    M = len(fpr)
    for i in range(M-1):
        AUC += (fpr[i+1]-fpr[i])*((tpr[i]+tpr[i+1])/2)
    return float(AUC)