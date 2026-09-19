import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # rng = np.random.default_rng(seed = seed)
    # x = np.asarray(x,dtype = float)
    # original_mean = np.mean(x)
    # n = len(x)
    # bootstrap_means = []
    # for i in range(n_bootstrap):
    #     bootstrap_sample = rng.choice(x, size=n, replace=True)
    #     bootstrap_means.append(float(np.mean(bootstrap_sample)))
    # bootstrap_means = np.asarray(bootstrap_means,dtype = float)
    # bootstrap_mean = np.mean(bootstrap_means)
    # alpha = (1-ci)/2
    # return {
    #     "bootstrap_mean" : float(bootstrap_mean),
    #     "lower": float(np.quantile(bootstrap_means,alpha)),
    #     "upper" : float(np.quantile(bootstrap_means,1-alpha))
    # }
    # vectorisation version 
    rng = np.random.default_rng(seed = seed)
    x = np.asarray(x,dtype = float)
    indices_randoming = rng.integers(0,x.size,size=(n_bootstrap,x.size))
    means = x[indices_randoming].mean(axis=1)
    alpha = (1-ci)/2
    return {
        "bootstrap_mean" : float(means.mean()),
        "lower": float(np.quantile(means,alpha)),
        "upper": float(np.quantile(means,1-alpha))
    }