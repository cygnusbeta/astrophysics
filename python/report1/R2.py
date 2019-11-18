# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(0, 6, 100)
    y = 4 * x ** 2 * np.exp(-2 * x)

    plt.plot(x, y, 'b')
    plt.grid(True, which="both", ls="--", color="g")

    plt.xlabel('r')
    plt.ylabel('ρ(r)')
    plt.show()


if __name__ == "__main__":
    main()
