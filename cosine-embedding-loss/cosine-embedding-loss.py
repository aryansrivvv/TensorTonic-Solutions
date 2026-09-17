import math

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    x1_x2 = 0 
    x1_x1 = 0 
    x2_x2 = 0 
    for i in range(len(x1)):
        x1_x2 += x1[i]*x2[i]
        x1_x1 += (x1[i])**2
        x2_x2 += (x2[i])**2
    sqx1 = math.sqrt(x1_x1)
    sqx2 = math.sqrt(x2_x2)
    cosx1x2 = (x1_x2)/(sqx1*sqx2)

    if label == 1 :
        return 1 - cosx1x2
    else:
        return max(0,cosx1x2-margin)