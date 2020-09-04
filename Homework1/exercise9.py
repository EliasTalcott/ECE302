#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plot

# Calculate the result of a matrix vector multiplication
def matrix_vector_multiplication():
    mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    vec = np.array([1, 2, 3])
    print("Result: {}".format(np.matmul(mat, vec)))


# Plot sine from -pi to pi with 1,000 data points
def plot_sine():
    x = np.linspace(-np.pi, np.pi, 1000)
    y = [np.sin(x_i) for x_i in x]
    plot.plot(x, y)
    plot.show()


# Plot 10,000 uniformly distributed random numbers on [0, 1)
def generate_histogram():
    x = np.random.uniform(0, 1, 10000)
    plot.hist(x)
    plot.show()


if __name__ == "__main__":
    matrix_vector_multiplication()
    plot_sine()
    generate_histogram()
