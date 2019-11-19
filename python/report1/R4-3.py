# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def main():
    x = [
        2.4397e3,
        6.0518e3,
        6.3710e3,
        3.3895e3,
        6.9911e4,
        5.8232e4,
        2.5362e4,
        2.4622e4
    ]
    y = [
        5.427,
        5.243,
        5.513,
        3.934,
        1.326,
        0.687,
        1.270,
        1.638
    ]
    labels = [
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune'
    ]

    plt.plot(x, y, 'bo')
    plt.grid(True, which="both", ls="--", color="g")
    for i, label in enumerate(labels):
        plt.text(x[i] + 2e3, y[i] + -1e-1, label, color="black", fontsize=9)


    plt.xlabel('Radius (km)')
    plt.ylabel('Density (g/cm3)')
    plt.show()


if __name__ == "__main__":
    main()
