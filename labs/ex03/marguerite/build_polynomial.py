# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    # ***************************************************
    poly = np.ones([len(x), degree+1])
    for row in range(len(x)): 
      for deg in range(degree+1):
        poly[row, deg]= x[row]**deg
    return poly
    # ***************************************************