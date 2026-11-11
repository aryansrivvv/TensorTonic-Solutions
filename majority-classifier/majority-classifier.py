import numpy as np

def majority_classifier(y_train: list, X_test: list) -> np.ndarray:
    """
    Returns a one-dimensional NumPy array.
    """
    y_train = np.asarray(y_train, dtype = 'float')
    X_test = np.asarray(X_test, dtype = 'float')
    classes, indices, counts = np.unique(y_train, return_index=True, return_counts=True)
    max_count = np.max(counts)
    is_max = (counts == max_count)
    best_idx = np.argmin(np.where(is_max, indices, np.inf))
    most_frequent_label = classes[best_idx]
    num_predictions = X_test.shape[0]
    return np.full(num_predictions, most_frequent_label, dtype=int)
    
    