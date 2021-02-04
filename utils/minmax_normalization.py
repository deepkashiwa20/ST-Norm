"""
    MinMaxNormalization
"""
from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility


class MinMaxNormalization(object):
    '''MinMax Normalization --> [-1, 1]
       x = (x - min) / (max - min).
       x = x * 2 - 1
    '''

    def __init__(self):
        pass

    def fit(self, X):
        self._min = X.min()
        self._max = X.max()
        self._logmin = np.log(X.min()+1)
        self._logmax = np.log(X.max()+1)
        print("min:", self._min, "max:", self._max, "logmin:", self._logmin, "logmax", self._logmax)

    def transform(self, X):
        # logX = np.log(X + 1)
        # X = 1. * (logX - self._logmin) / (self._logmax - self._logmin)
        X = 1. * (X - self._min) / (self._max - self._min)
        X = X * 2. - 1.
        return X

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X):
        X = (X + 1.) / 2.
        X = 1. * X * (self._max - self._min) + self._min
        # X = 1. * X * (self._logmax - self._logmin) + self._logmin
        # expX = np.exp(X) - 1
        # print(expX)
        return X


class MinMaxNormalization_01(object):
    '''MinMax Normalization --> [0, 1]
       x = (x - min) / (max - min).
    '''

    def __init__(self):
        pass

    def fit(self, X):
        self._min = X.min()
        self._max = X.max()
        print("min:", self._min, "max:", self._max)

    def transform(self, X):
        X = 1. * (X - self._min) / (self._max - self._min)
        return X

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def inverse_transform(self, X):
        X = 1. * X * (self._max - self._min) + self._min
        return X