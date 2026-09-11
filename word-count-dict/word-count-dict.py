def word_count_dict(sentences: list) -> dict:
    """
    Returns a dictionary of token counts.
    """
    res = {}
    for i in sentences:
        for j in i:
            if(j in res):
                res[j]+=1
            else:
                res[j] = 1
    return res