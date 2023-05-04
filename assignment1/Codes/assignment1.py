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
# list of pmf values
dist0 = [binom.pmf(0, n, p)]
dist1 = [binom.pmf(1, n, p)]
dist2 = [binom.pmf(2, n, p)]
# plotting the graph
plt.bar(0, dist0)
plt.bar(1, dist1)
plt.bar(2, dist2)
plt.show()
