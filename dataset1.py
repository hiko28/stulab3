import numpy as np


def true_function(x):
    y = np.sin(np.pi * x * 0.8)
    '''
    >>>true_function(0)
    0
    '''
    return y


if __name__ == '_main_':
    import doctest

    doctest.testmod()
