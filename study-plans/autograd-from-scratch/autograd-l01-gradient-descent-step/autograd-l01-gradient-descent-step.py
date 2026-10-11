import numpy as np

def gradient_descent_step(values: list, gradients: list, learning_rate: float) -> tuple[list, float]:
    """
    Returns a fresh list of updated values and the predicted objective change.
    """
    pass
    l = len(values)
    if (l==0):
        return ([] , 0.0)

    values = np.asarray(values, dtype = 'float')
    gradients= np.asarray(gradients, dtype = 'float')

    updated_list = values - learning_rate*gradients
    delta_L_pred = -float(learning_rate*np.sum(gradients**2, dtype = float))

    return (updated_list.tolist() , delta_L_pred)
