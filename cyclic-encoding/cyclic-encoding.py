import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    # Write code here
    final_values = []
    for i in values:
        theta = (2*math.pi*i)/period
        x = [math.sin(theta), math.cos(theta)]
        final_values.append(x)
    return final_values