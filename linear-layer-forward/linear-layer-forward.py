def linear_layer_forward(X: list, W: list, b: list) -> list:
    """
    Returns the affine transformation for every input row.
    """
    n  = len(X)
    d_in = len(X[0])
    d_out = len(W[0])
    X_W = [[0 for i in range(d_out)] for j in range(n)]
    for i in range(n):
        for j in range(d_out):
            for k in range(d_in):
                X_W[i][j] += X[i][k]*W[k][j]
            X_W[i][j] += b[j]
    return X_W
                