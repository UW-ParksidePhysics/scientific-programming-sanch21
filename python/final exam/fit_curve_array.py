__author__ = 'Adrian Sanchez'
import numpy as np


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, data_points=50):
    if maximum_x < minimum_x:
        raise ArithmeticError
    if data_points <= 2:
        raise IndexError
    x_array = np.linspace(minimum_x, maximum_x, data_points)
    y_array = np.polyval(quadratic_coefficients, x_array)
    fit_curve = np.array((x_array, y_array))
    return fit_curve


