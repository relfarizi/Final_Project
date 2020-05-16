from pymoo.interface import crossover
from pymoo.factory import get_crossover
import numpy as np
import matplotlib.pyplot as plt

def example_parents(n_matings, n_var):
    a = np.arange(n_var)[None, :].repeat(n_matings, axis=0)
    b = a + n_var
    return a, b


def show(M):
    plt.figure(figsize=(4,4))
    plt.imshow(M, cmap='Greys',  interpolation='nearest')
    plt.xlabel("Variables")
    plt.ylabel("Individuals")
    plt.show()

n_matings, n_var = 10, 10
a,b = example_parents(n_matings,n_var)
#print(a,b)
print("One Point Crossover")
print(get_crossover("bin_one_point"))
off = crossover(get_crossover("bin_one_point"), a, b)
print(len(off))
#show((off[:n_matings] != a[0]))