# importing required libraries
from fractions import Fraction
from scipy.stats import binom
import matplotlib.pyplot as plt
# simulating random variable X
# setting the values of n and p
n = 2          #number of trails
p='4/9'        #probability of success
p=Fraction(p)  #change the type of x from string to Fraction
p=float(p)     #change the type of x from Fraction to float
# defining list of r values
r_values = list(range(n + 1))
# list of pmf values
dist = [binom.pmf(r, n, p) for r in r_values ]
# plotting the graph
plt.bar(r_values, dist)
plt.show()
