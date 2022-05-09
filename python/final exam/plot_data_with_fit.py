__author__ = 'Frank Lauerman'
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format='o', fit_format=''):
    scatter_plot = plt.plot(data[0, :], data[1, :], data_format)
    best_fit = plt.plot(fit_curve[0, :], fit_curve[1, :], fit_format)
    return scatter_plot, best_fit

