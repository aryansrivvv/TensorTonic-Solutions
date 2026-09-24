import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    X = np.asarray(X,dtype = float) 
    n, d = X.shape # n rows and d columns 
    mean_of_features = np.mean(X,axis = 0) # (d,1) array of mean of each feature/column
    centered_mean = X - mean_of_features # a new array consisting of centered values
    column_stds = np.std(centered_mean, axis=0 , ddof = 1) # sample standard deviations 
    std_outer = np.outer(column_stds,column_stds) # outer product 
    covariance_matrix = np.dot(centered_mean.T , centered_mean , ) / (n-1)
    corr_matrix = np.full_like(covariance_matrix, np.nan)
    np.divide(covariance_matrix,std_outer,out = corr_matrix , where = (std_outer>0))
    return corr_matrix
    
    
    