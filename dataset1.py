import numpy as np


def true_function(x):
    y = np.sin(np.pi * x * 0.8)
    '''
    >>>true_function(0)
    0
    '''
    return y


# テスト
if __name__ == '_main_':
    import doctest

    doctest.testmod()

# 描画
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.1)
y = np.sin(np.pi * x * 0.8)
plt.plot(x, y)
plt.show()
