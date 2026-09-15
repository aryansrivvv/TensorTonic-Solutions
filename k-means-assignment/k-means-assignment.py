def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    res = []
    len_points = len(points)
    len_centroids = len(centroids)
    d = len(points[0])
    for i in range(len_points):
        min_dist = float('inf')
        index = 0
        for j in range(len_centroids):
            dist = 0
            for k in range(d):
                dist += (points[i][k]-centroids[j][k])**2
            if(dist<min_dist):
                min_dist = dist
                index = j
        res.append(index)
    return res