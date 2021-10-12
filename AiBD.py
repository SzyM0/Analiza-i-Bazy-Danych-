#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
import numpy as np
from matplotlib import pyplot as plt


def fun(x):
    return x**2 + 5


arg1 = np.linspace(-1, 1, 100)
arg2 = np.linspace(-6, 6, 600)
arg3 = np.linspace(0, 5, 500)


fig, ax = plt.subplots(3, 1)

ax[0].plot(arg1, fun(arg1))
ax[0].set_title("(-1 , 1)")
ax[0].set_ylabel("y")
ax[0].set_xlabel("x")

ax[1].plot(arg2, fun(arg2))
ax[1].set_title("(-6, 6)")
ax[1].set_ylabel("y")
ax[1].set_xlabel("x")

ax[2].plot(arg3, fun(arg3))
ax[2].set_title("(0, 5)")
ax[2].set_ylabel("y")
ax[2].set_xlabel("x")


plt.show()


