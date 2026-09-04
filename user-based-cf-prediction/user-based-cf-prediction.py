def user_based_cf_prediction(similarities: list, ratings: list) -> float:
    """
    Returns the positive-similarity weighted rating prediction.
    """
    # Write code here
    weighted_sum = 0 
    positive_similarity_sum = 0
    l = len(similarities)
    for i in range(l):
        if(similarities[i]>0):
            weighted_sum+= similarities[i]*ratings[i]
            positive_similarity_sum+=similarities[i]

    if positive_similarity_sum == 0:
        return 0.0
    return float(weighted_sum/positive_similarity_sum)