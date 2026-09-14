import math

def log_loss(y_true: list, y_pred: list, eps: float = 1e-15) -> list:
    """
    Returns a list of loss values.
    """
    log_loss = []
    l = len(y_true)
    for i in range(l):
        p_hat = min(1-eps, max(eps,y_pred[i]))
        L_y_p = -(y_true[i]*math.log(p_hat)+(1-y_true[i])*math.log(1-p_hat))
        log_loss.append(L_y_p)
    return log_loss
        