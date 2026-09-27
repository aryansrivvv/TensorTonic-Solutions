import numpy as np

def epsilon_greedy(q_values: list, epsilon: float, seed: int = 0) -> int:
    """
    Returns the action index as an integer.
    """
    q_values = np.asarray(q_values, dtype = float)
    rng = np.random.default_rng(seed)
    x = rng.random()
    if( x < epsilon):
        return int(rng.integers(q_values.size))
    else:
        return int(np.argmax(q_values))
    