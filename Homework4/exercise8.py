#!/usr/bin/env python

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plot

def generateRealization(arr):
    return arr * rand(len(arr))

def plotPmf(data):
    plot.bar(x=[1, 2, 3, 4, 5, 6, 7], height=data)
    plot.xlabel("x")
    plot.ylabel("Frequency (%)")
    plot.title("10,000 realizations of a discrete PMF")
    plot.savefig("histogram.png")


if __name__ == "__main__":
    numRealizations = 10000
    pmf = np.array([0.3, 0.1, 0.15, 0.25, 0.1, 0.08, 0.02])
    realizations = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    # Generate realizations of the discrete pmf generated above
    for _ in range(numRealizations):
        realizations += generateRealization(pmf)
    realizations /= sum(realizations)

    # PLot the realizations in a histogram
    plotPmf(realizations)
