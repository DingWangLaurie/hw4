# Question 1.1

import warnings
import numpy as np
import matplotlib.pyplot as plt
from numpy import newaxis

warning.filterwarnings("ignore") # to suppress square overflow warnings

def mandelbrot(N_max, threshold, n):
    """
    Calculates and returns the Mandelbrot set
    :param int N_max: maximum number of Mandelbrot iterations
    :param float threshold: the threshold value to calculate the Mandelbrot set
    :param int n: the length of the Mandelbrot set
    
    returns mask: 2D array of size nxn, the calculated mandelbrot set
    """

    # Create a 1D array of size n, ranging values from -2 to 1
    x = np.linspace(-2,1,n)
    # Create a 1D array of size n, ranging values from -1.5 to 1.5
    y = np.linspace(-1.5,1.5,n)

    # Create the nxn grid between range [-2,1] x [-1.5,1.5]
    c = x[:,newaxis] +1j*y[newaxis,:]

    # Store the c grid in z
    z = c

    # Apply the MandelBrot iteration for N_max steps
    for j in range(N_max):
        z = z**2 + c
    
    # Create a 3D boolean matrix mask, which checks if |z| < threshold
    mask = (abs(z) < threshold)

    return mask
# Calls the mandelbrot funcftion
mask = mandelbrot(N_max=50, threshold=50., n=600)

# Plotting and saving the figure as mandelbrot.png
plt.imshow(masj.T,extent=[-2,1,-1.5,1.5])
plt.gray()
plt.savefig("mandelbrot.png")

# Question 1.2
