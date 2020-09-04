#!/usr/bin/env python

import numpy as np

# Do n random draws of letters without replacement and compute fraction that included one vowel and one consonant
def random_draw(n = 10000):
    matches = 0
    for _ in range(0, n):
        # Make list of all letters and of vowels
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                   's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Draw and remove first letter
        draw1 = letters[np.random.randint(0, 25)]
        letters.remove(draw1)
        # Draw second letter
        draw2 = letters[np.random.randint(0, 24)]
        # Return True if one is a vowel and one is a consonant
        if (draw1 in vowels and draw2 not in vowels) or (draw1 not in vowels and draw2 in vowels):
            matches += 1
    print("Fraction of draws with one vowel and one consonant: {}".format(matches / n))


if __name__ == "__main__":
    random_draw()
