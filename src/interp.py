# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 15:07:32 2014

@author: Andreea
"""
from __future__ import print_function
from __future__ import division
import numpy as np

class interp1d:
    '''
    This is based off of scipy.interpolate.interp1d, but lacks most of the checks and robustness
    of the scipy version.
    It is a bit faster, but must be run correctly (undefined behavior otherwise).
    Input for initialization:
        two numpy.arrays x and y sorted in increasing order by x.
    '''
    def __init__(self, x, y, kind = "linear", fill_value = np.nan):
        self.x = x
        self.y = y
        self.len = len(self.x)
        self.fill_value = fill_value
        if kind == "linear":
            self._call = self._call_linear
        else:
            raise NotImplementedError("This kind is unsupported!")

    def __call__(self, x_new):
        return self._evaluate(x_new)

    def _check_bounds(self, x_new):
        below_bounds = x_new < self.x[0]
        above_bounds = x_new > self.x[-1]
        if below_bounds:
            raise ValueError("A value in x_new is below the interpolation range.")
        if above_bounds:
            raise ValueError("A value in x_new is above the interpolation range.")
        out_of_bounds = np.logical_or(below_bounds, above_bounds)
        return out_of_bounds

    def _evaluate(self, x_new):
        out_of_bounds = self._check_bounds(x_new)
        if out_of_bounds:
            y_new = self.fill_value
        else:
            y_new = self._call(x_new)
        return y_new

    def _call_linear(self, x_new):
        x_new_index = np.searchsorted(self.x, x_new)
        x_new_index = x_new_index.clip(1, self.len-1).astype(int)
        lo = x_new_index - 1
        hi = x_new_index
        x_lo = self.x[lo]
        x_hi = self.x[hi]
        y_lo = self.y[lo]
        y_hi = self.y[hi]
        slope = (y_hi - y_lo) / (x_hi - x_lo)
        y_new = slope*(x_new - x_lo) + y_lo
        return y_new