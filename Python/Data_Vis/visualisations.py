"""visualisations.py
   Basic test case to plot some curves"""

#%% Imports
import matplotlib.pyplot as plt
from math import log2, factorial
import statistics


#%% Function block - lists of values for various scaling functions used in Big O
x_vals = range(1, 100)

linear = [x for x in x_vals]  # n
logarithmic = [log2(x) for x in x_vals]  # log n
lin_log = [(x * log2(x)) for x in x_vals]  # n log n
quadratic = [x ** 2 for x in x_vals]  # n^2
exponential = [2 ** x for x in x_vals]  # 2^n
fact = [factorial(x) for x in x_vals]  # n!

myfuns = {
    "n": linear,
    "log n": logarithmic,
    "n log n": lin_log,
    "n^2": quadratic,
    "2^n": exponential,
    "n!": fact,
}


#%% Render block

# Dimensions of plot
fig = plt.figure(figsize=(8, 6))

# Add each function line from the above dictionary
for fun_name, y_vals in myfuns.items():
    plt.plot(x_vals, y_vals, label=f"{fun_name}")

# Log axes
# plt.loglog(basex=10,basey=2)

plt.legend()
plt.show()
