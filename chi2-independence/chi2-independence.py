import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    C = np.asarray(C,dtype = float)
    
    row_sums = np.sum(C, axis=1)
    column_sums = np.sum(C, axis=0)
    total_sum = np.sum(row_sums)
    
    resultant_matrix = np.outer(row_sums, column_sums) / total_sum
    

    chi2 = np.sum(((C - resultant_matrix) ** 2) / resultant_matrix)
    return {
        "chi2": float(chi2), 
        "expected" : resultant_matrix 
    }
    
    