import matplotlib.pyplot as plt
import numpy as np
import time

def primeSieve(n):

    numbers = []
    for i in range(2, n+1): numbers.append(i)
    
    for i in range(2, n+1):

        j = 2
        t = i*j

        while t <= n: 
            if numbers.count(t) > 0: numbers.remove(t)
            j += 1
            t = i*j
  
    return numbers

input = []
times = []

for i in range(10000, 50000, 5000):
    tic = time.perf_counter()
    primes = primeSieve(i)
    toc = time.perf_counter()
    input.append(i)
    times.append(toc - tic)
    print(f"{i}: {toc - tic:0.4f} seconds")

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(input, times)  # Plot some data on the axes.

plt.show()