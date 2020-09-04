#!/usr/bin/env python

import numpy as np

# Do m runs of n students with random birthdays to determine probability of collision
def birthday_problem(m = 10000, n = 50):
    matches = 0
    for _ in range(0, m):
        # Assign each student a random birthday between 0 and 364
        students = np.random.randint(0, 365, n)
        # Checks for birthday matches since set doesn't contain duplicates
        if len(students) != len(set(students)):
            matches += 1
    print("Fraction of simulations with at least one matching birthday: {}".format(matches / m))


if __name__ == "__main__":
    birthday_problem()