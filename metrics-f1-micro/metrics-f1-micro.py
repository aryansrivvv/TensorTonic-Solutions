def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    TP = 0 
    FP = 0 
    for i in range(len(y_true)):
        if(y_pred[i] == y_true[i]):
            TP+=1
        else:
            FP+=1
    return float(TP/(TP+FP))
            
            
        