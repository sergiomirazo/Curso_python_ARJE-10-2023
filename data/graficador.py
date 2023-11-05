import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_title('Movimiento browniano')
ax.set_xlabel('Posición en x')
ax.set_ylabel('Posición en y')

plt.show()
