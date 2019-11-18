# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def t(theta):
    print(t)
    return np.sin(theta) + theta


def r(theta):
    return (1 + np.cos(theta)) / 2


def main():
    t_range = np.arange(0, np.pi, np.pi / 100)

    plt.plot(t(t_range), r(t_range))
    plt.xlabel('t(θ)')
    plt.ylabel('R(θ)')
    plt.show()


if __name__ == "__main__":
    main()
