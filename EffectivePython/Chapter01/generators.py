import numpy as np
import time

# This creates a large file (193 MB) with random numbers
with open('example.txt', 'w') as f:
    for i in range(10000000):
        f.write(str(np.random.uniform()) + '\n')


tic = time.time()
it = (float(x) for x in open('example.txt'))
print(it)
print(next(it))
print(next(it))
print(next(it))
roots = ((x, x**0.5) for x in it)
print(next(roots))
toc = time.time()
print('Required time: ' + str(toc-tic))


tic = time.time()
ls = [float(x) for x in open('example.txt')]
print(ls[0])
toc = time.time()
print('Required time: ' + str(toc-tic))
