import numpy as np

def pca_projection(X: list, k: int) -> list:
    """
    Returns the centered data projected onto the top components.
    """
    X = np.asarray(X, dtype = 'float')
    X_centered = X - X.mean(axis = 0)
    covar_X = np.cov(X_centered , y = None , rowvar = False, bias = True , ddof = 1)
    eigenvalues , eigenvectors = np.linalg.eigh(covar_X)
    idx = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[idx]
    sorted_eigenvectors = eigenvectors[:, idx]
    top_k_eigenvalues = sorted_eigenvalues[:k]
    top_k_eigenvectors = sorted_eigenvectors[:, :k]
    return list(np.dot(X_centered, top_k_eigenvectors))