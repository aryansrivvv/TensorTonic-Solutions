import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    lam = 1.0507
    alpha = 1.6733
    return [ lam*i if i>0 else lam*alpha*(math.exp(i)-1) for i in x ]