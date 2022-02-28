#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# linear graph
#  plt.plot([1, 2, 3, 4])
#  plt.ylabel('some numbers')
#  plt.show()

# HISTOGRAM
#  mu, sigma = 100, 15
#  x = mu + sigma * np.random.randn(10000)

# the histogram of the data
#  n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


#  plt.xlabel('Smarts')
#  plt.ylabel('Probability')
#  plt.title('Histogram of IQ')
#  plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#  plt.axis([40, 160, 0, 0.03])
#  plt.grid(True)
#  plt.show()

# CATEGORICAL VARIABLES
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3)) # specify width and height in inches

plt.subplot(131)           # equiv to subplot((1,3,1)) tuple = (nrows, ncols, index) 
plt.bar(names, values)     # so place plot the first position of and take 1 row and 3 cols
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')

# so we have 3 figures which take 3 cols (inchs) each and figure of 9 cols (inches)
# and each figure is 3 high, and we have 3 rows (inchs) so it all makes sense.
plt.show()


