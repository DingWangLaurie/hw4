# Question 1.2

import numpy as np
import random as rm
from random import seed
from random import random

import matplotlib.pyplot as plt

def phat_minus_ps(n=5, N=50):
  p = np.random.rand(n)
  p /= p.sum()
  
  P = np.random.rand(n**2).reshape(n, n)
  P = P/P.sum(1).reshape(-1, 1)
  
  lamb, V = np.linalg.eig(P.T)
  nu = V[:, 0]/V[:, 0].sum()
  
  err = []
  for i in range(N):
    p = (P.T)@p
    err.append(float(( ((nu.flatten()-p.flatten())**2)**(1/2)).sum() ))
    
  plt.plot(list(range(N)), err)
  plt.show()
  plt.savefig('markov_estimation_error.png', dpi=300)

phat_minus_ps(50, 10)