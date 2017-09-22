import numpy as np
vector1 = np.random.random(15)
print('Initial vector is\n')
print(vector1)
vector1[vector1.argmax()]=100
print('Modified vector is\n')
print(vector1)


