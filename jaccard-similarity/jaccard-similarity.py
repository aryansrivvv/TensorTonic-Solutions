def jaccard_similarity(set_a: list, set_b: list) -> float:
    """
    Returns the Jaccard similarity of the two item collections.
    """
    a = set(set_a)
    b = set(set_b)
    int_l = len(a & b)
    uni_l = len( a | b)
    if (uni_l == 0 ):
        return 0.0
    return float(int_l/uni_l)