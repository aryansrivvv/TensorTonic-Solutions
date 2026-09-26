import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    ELU = []
    for i in x:
        if (i > 0 ):
            ELU.append(i)
        else:
            ELU.append(alpha*(math.exp(i)-1))
    return ELU