# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

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
        3.3010e23,
        4.8673e24,
        5.9722e24,
        6.4169e23,
        1.8981e27,
        5.6832e26,
        8.6810e25,
        1.0241e26
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
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", color="g")
    for i, label in enumerate(labels):
        plt.text(1.1 * x[i], 0.9 * y[i], label, color="black", fontsize=9)
    plt.show()


if __name__ == "__main__":
    main()
