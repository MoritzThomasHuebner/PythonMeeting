import numpy as np
import time

# with open('example.txt', 'w') as f:
#     for i in range(100000000):
#         f.write(str(np.random.uniform()) + '\n')

tic = time.time()
it = (float(x) for x in open('example.txt'))
print(it)

roots = ((x, x**0.5) for x in it)

with open('test.txt', 'w') as f:
    for root in roots:
        f.write(root)
toc = time.time()
print('Required time: ' + str(toc-tic))


tic = time.time()
ls = [float(x) for x in open('example.txt')]
print(ls[0])
with open('test_2.txt', 'w') as f:
    f.write([x, x**0.5])

toc = time.time()
print('Required time: ' + str(toc-tic))
