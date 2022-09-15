###################### MATPLOTLIB.PYPLOT #########################

""" pyplot_ext1.py
    Pyplot Three from https://matplotlib.org/stable/gallery/index.html"""

import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = [i/5 for i in range(0, 25)]
t_sq = [i**2 for i in t]
t_cube = [i**3 for i in t]

# red, blue and green lines with legends
plt.plot(t, t, "r", label="y=x linear")
plt.plot(t, t_sq, "b", label="y=x^2 quadratic")
plt.plot(t, t_cube, "g", label="y=x^3 cubed")
plt.legend()  # needed to show the legend

plt.show()



###################### NUMPY ##########################

""" pyplot_numpy.py
    Pyplot Three from https://matplotlib.org/stable/gallery/index.html"""
import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
# while range() only works with integer steps,
# np.arange() allows decimal steps. Creates an "ndarray", not a list
t = np.arange(0., 5., 0.2)

# red circles, blue squares with line and green triangles
plt.plot(t, t, "ro", t, t**2, "bs-", t, t**3, "g^")
plt.show()