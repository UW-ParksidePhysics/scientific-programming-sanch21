__author__ = 'Adrian Sanchez'
import numpy as np


def fit_curve_array(quadratic_coefficients, minimum_x, maximum_x, data_points=50):
    '''

    :param quadratic_coefficients: ndarray, shape (3,)
    Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
    :param minimum_x:float
    Starting value for the fit_curve array
    :param maximum_x:float
    Ending value for the fit curve array
    :param data_points: int, optional
    Number of points N to return for final fit curve. Default is 100.
    :return:
    '''
    if maximum_x < minimum_x:
        raise ArithmeticError
    if data_points <= 2:
        raise IndexError
    x_array = np.linspace(minimum_x, maximum_x, data_points)
    y_array = np.polyval(quadratic_coefficients, x_array)
    fit_curve = np.array((x_array, y_array))
    return fit_curve


