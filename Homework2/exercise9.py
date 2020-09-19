#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Roll an mxn array of dice
def roll_m_by_n_dice(m, n):
    return np.random.randint(1, 7, (m, n))


# Make a histogram with bins 1-6 of an array of dice rolls
def plot_rolls_array(arr, low, high, title):
    flatboi = [item for sublist in arr for item in sublist]
    bins = np.linspace(low, high+1, num=high-low+2)
    plt.hist(flatboi, bins=bins, align="left", rwidth=0.9)
    plt.title(title)
    plt.savefig(title+".pdf")
    plt.clf()

    # Calculate probability for Part E
    if title == "Part D":
        goodbois = 0
        totalbois = len(flatboi)
        for num in flatboi:
            if num > 4 and num <= 7:
                goodbois += 1
        print("Probability of higher than 4 and less than or equal to 7: {}".format(goodbois / totalbois))


if __name__ == "__main__":
    # Part A
    x_1 = roll_m_by_n_dice(1, 100)
    plot_rolls_array(x_1, 1, 6,"Part A")

    # Part B
    x_2 = roll_m_by_n_dice(10000, 100)
    plot_rolls_array(x_2, 1, 6, "Part B")

    # Part C
    y_1 = roll_m_by_n_dice(1, 100)
    z_1 = x_1 + y_1
    plot_rolls_array(z_1, 2, 12, "Part C")

    # Part D
    y_2 = roll_m_by_n_dice(10000, 100)
    z_2 = x_2 + y_2
    plot_rolls_array(z_2, 2, 12, "Part D")

    # Part F
    z_3 = roll_m_by_n_dice(1, 10000)
    for i in range(9):
        z_3 += roll_m_by_n_dice(1, 10000)
    plot_rolls_array(z_3, 10, 60, "Part F")

    # Part G
    z_4 = roll_m_by_n_dice(1, 10000)
    for i in range(99):
        z_4 += roll_m_by_n_dice(1, 10000)
    plot_rolls_array(z_4, 100, 600, "Part G")